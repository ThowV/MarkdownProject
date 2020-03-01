from PyQt5.QtWebEngineWidgets import QWebEngineView


class EditorPreviewInstanceWidget(QWebEngineView):
    def __init__(self, parent=None):
        super(EditorPreviewInstanceWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Preview content
        self.setObjectName("PreviewWebEngineWidget")

    def update_html(self, html):
        self.setHtml(html)
