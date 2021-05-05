from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class CategoryPage(Page):
    """Section page."""

    content_panels = Page.content_panels

    class Meta:
        verbose_name = _("Category page")
        verbose_name_plural = _("Category pages")

    parent_page_types = ["home.HomePage"]
    subpage_types: list = ["article.SectionPage"]


class SectionPage(Page):
    """Section page."""

    content_panels = Page.content_panels

    class Meta:
        verbose_name = _("Section page")
        verbose_name_plural = _("Section pages")

    parent_page_types = ["article.CategoryPage"]
    subpage_types: list = ["article.ArticlePage"]


class ArticlePage(Page):
    """Article page."""

    article_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        verbose_name=_("article image"),
    )
    content = RichTextField(
        blank=False,
        null=True,
        verbose_name=_("article content"),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("article_image"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = _("Article page")
        verbose_name_plural = _("Article pages")

    parent_page_types = ["article.SectionPage"]
    subpage_types: list = []
