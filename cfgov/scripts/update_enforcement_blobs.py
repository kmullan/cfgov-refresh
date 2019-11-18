from __future__ import unicode_literals
from re import search, IGNORECASE

from v1.models import DocumentDetailPage
from v1.util.migrations import get_stream_data, set_stream_data
from v1.tests.wagtail_pages.helpers import publish_changes

def update_sidefoot():
    draft_pages = []
    for page in DocumentDetailPage.objects.all():
        url = page.get_url()

        if not page.live:
            continue
        if 'policy-compliance/enforcement/actions' not in url:
            continue
        if page.has_unpublished_changes:
            draft_pages.append(url)
            continue

        stream_data = get_stream_data(page, 'sidefoot')

        for field in stream_data:
            if field['type'] == 'related_metadata':
                field_content = field['value']['content']
                new_content = []
                for block in field_content:
                    # Switch File number to Docker number
                    if block['value'].get('heading', '') == 'File number':
                        block['value']['heading'] = 'Docket number'
                    # Remove inline Category, use the page category instead
                    if block['value'].get('heading', '') != 'Category':
                        new_content.append(block)
                field['value']['content'] = new_content
            break
        set_stream_data(page.specific, 'sidefoot', stream_data)
    if len(draft_pages) > 0:
        print('Skipped the following draft pages:', ' '.join(draft_pages))
    else:
        print('No draft pages found, updates made to all valid enforcement actions pages')


def run():
    update_sidefoot()
