

(function() {
	//connect to the "SaveAssist" app.
	var port = browser.runtime.connectNative("SaveAssist");
	/**
	* Check and set a global guard variable.
	* If this content script is injected into the same page again,
	* it will do nothing next time.
	*/
	if (window.hasRun) {
		return;
	}
	window.hasRun = true;
	
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
				console.log("You clicked 'Save'.");
				sendString = "Save<" + info.srcUrl
				console.log("Sending: " + sendString);
				port.postMessage(sendString);
			break;
			case "SaveAssistSaveAs":
				console.log("You clicked 'SaveAs'.");
				sendString = "SaveAs<" + info.srcUrl
				console.log("Sending: " + sendString);
				port.postMessage(sendString);
			break;
			
		}
	})
  

})();