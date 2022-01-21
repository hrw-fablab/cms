from django.utils.safestring import mark_safe

from wagtail.core import hooks

# Until 2.16 (Will be supported nativ) Override collapsible for StructBlocks
@hooks.register('insert_editor_js')
def editor_js():

    return mark_safe(
        """
        <script>
          document.addEventListener('DOMContentLoaded', function () {
              const blocks = document.querySelectorAll('div.c-sf-block__content[aria-hidden="false"]');
  
              blocks.forEach(function(block) {
                  block.parentNode.querySelector('.c-sf-block__header').dispatchEvent(new MouseEvent("click"));
              });
          });
        </script>
        """
    )