from abstract.pages.folder import AbstractFolderPage

class FolderPage(AbstractFolderPage):
	parent_page_types = ["Homepage"]
	subpage_type = ["ArticleIndexPage", "ProjectIndexPage", "DeviceIndexPage"]