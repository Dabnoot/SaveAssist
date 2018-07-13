(function() {
	/**
	* Check and set a global guard variable.
	* If this content script is injected into the same page again,
	* it will do nothing next time.
	*/
	if (window.hasRun) {
		return;
	}
	window.hasRun = true;
	
	var iImageCount = 0;
	var sLastFolder = "";
	var sLastSrcURL = "";
	
	browser.contextMenus.create({
		id: "SaveAssistSave",
		title: "Quick Save",
		contexts: ["image"]
	});
	
	browser.contextMenus.create({
		id: "SaveAssistSaveAs",
		title: "Quick Save As...",
		contexts: ["image"]
	});

	browser.contextMenus.onClicked.addListener(function(info, tab) {
		switch (info.menuItemId) {
			case "SaveAssistSave":
				console.log("You clicked 'Save'.", iImageCount);
				console.log(info.srcUrl);
			break;
			case "SaveAssistSaveAs":
				console.log("You clicked 'SaveAs'.");
			break;
			
		}
	})
  

})();