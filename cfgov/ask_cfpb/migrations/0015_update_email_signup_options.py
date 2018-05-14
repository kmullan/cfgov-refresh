# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailsnippets.blocks
import v1.blocks
import v1.models.snippets
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0014_recreated_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerpage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField([('call_to_action', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False)), (b'size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'regular', b'Regular'), (b'large', b'Large Primary')]))]))])), ('related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), ('related_metadata', wagtail.wagtailcore.blocks.StructBlock([(b'slug', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'content', wagtail.wagtailcore.blocks.StreamBlock([(b'text', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'blob', wagtail.wagtailcore.blocks.RichTextBlock())], icon=b'pilcrow')), (b'list', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))], icon=b'list-ul')), (b'date', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'date', wagtail.wagtailcore.blocks.DateBlock())], icon=b'date')), (b'topics', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(default=b'Topics', max_length=100)), (b'show_topics', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False))], icon=b'tag'))])), (b'is_half_width', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))])), ('email_signup', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'default_heading', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', default=True, required=False, label=b'Default heading style')), (b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'gd_code', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'form_field', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'btn_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'required', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'info', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Disclaimer')), (b'inline_info', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Show disclaimer on same line as button. Only select this option if the disclaimer text is a few words (ie, "Privacy Act statement") rather than a full sentence.', required=False, label=b'Inline disclaimer')), (b'label', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'type', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'text', b'Text'), (b'checkbox', b'Checkbox'), (b'email', b'Email'), (b'number', b'Number'), (b'url', b'URL'), (b'radio', b'Radio')])), (b'placeholder', wagtail.wagtailcore.blocks.CharBlock(required=False))]), required=False, icon=b'mail'))])), ('sidebar_contact', wagtail.wagtailcore.blocks.StructBlock([(b'contact', wagtail.wagtailsnippets.blocks.SnippetChooserBlock(b'v1.Contact')), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Add a horizontal rule line to top of contact block.', default=False, required=False))])), ('rss_feed', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'blog_feed', b'Blog Feed'), (b'newsroom_feed', b'Newsroom Feed')])), ('social_media', wagtail.wagtailcore.blocks.StructBlock([(b'is_share_view', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If unchecked, social media icons will link users to official CFPB accounts. Do not fill in any further fields.', default=True, required=False, label=b'Desired action: share this page')), (b'blurb', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Sets the tweet text, email subject line, and LinkedIn post text.', default=b"Look what I found on the CFPB's site!", required=False)), (b'twitter_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom text for Twitter shares. If blank, will default to value of blurb field above.', max_length=100, required=False)), (b'twitter_related', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) A comma-separated list of accounts related to the content of the shared URL. Do not enter the  @ symbol. If blank, it will default to just "cfpb".', required=False)), (b'twitter_hashtags', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) A comma-separated list of hashtags to be appended to default tweet text.', required=False)), (b'twitter_lang', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Loads text components in the specified language, if other than English. E.g., use "es"  for Spanish. See https://dev.twitter.com/web/overview/languages for a list of supported language codes.', required=False)), (b'email_title', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom subject for email shares. If blank, will default to value of blurb field above.', required=False)), (b'email_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom text for email shares. If blank, will default to "Check out this page from the CFPB".', required=False)), (b'email_signature', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Adds a custom signature line to email shares. ', required=False)), (b'linkedin_title', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom title for LinkedIn shares. If blank, will default to value of blurb field above.', required=False)), (b'linkedin_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom text for LinkedIn shares.', required=False))])), ('reusable_text', v1.blocks.ReusableTextChooserBlock(v1.models.snippets.ReusableText))], blank=True),
        ),
    ]
