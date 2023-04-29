AJAX Framework Version 2.3
Copyright 2005 GodLikeMouse http://www.godlikemouse.com

Overview:

The AJAX Framework is a cross browser framework that allows developers to
quickly develop web pages that can call web services and server pages through
javascript without having to submit the current page.

For more information and troubleshooting help, please go to:
http://sourceforge.net/docman/?group_id=136362


Terms of Use:

The AJAX Framework is free to use in any and all projects under the GNU Open
Source License so long as the header of the AJAX.js page remains intact.


Usage:

To start using the AJAX Framework simply create any type of web page and
include <SCRIPT language="JavaScript" src="script/glm-ajax.js"></SCRIPT> in the
<HEAD> of the document.

To make a call using the AJAX Framework simple instanciate the AJAX class "var
ajax = new GLM.AJAX();" and call the appropriate call method.  For web services
use "callService()", for page calls use "callPage()".

The callService method will invoke the web service passed in and return the
content of the response.

The callPage method will call the page passed in and return the HTML in the
body of the document.



For up to date documetation please visit:    http://www.godlikemouse.com/glm-ajax


Examples:

callPage example:
--------------------------------------------------------
function pageCallback(response){
	alert(response);
}


var ajax = new GLM.AJAX();
ajax.callPage("mypage.html", pageCallback);



serviceCall example:
--------------------------------------------------------
function serviceCallback(response){
	alert(response);
}


var ajax = new GLM.AJAX();
ajax.callService("http://myserver.com/MyWebService.asmx", "MyMethodToCall", serviceCallback);


serviceCall with parameters example:
--------------------------------------------------------
function serviceCallback(response){
	alert(response);
}

var ajax = new GLM.AJAX();
/* paramters are added to the end of the callService method in key=value pairs. */
ajax.callService("http://myserver.com/MyWebService.asmx", "MyMethodToCall", serviceCallback, "myParameter1=hello", "myParameter2=world");


serviceCall with custom namespace example:
--------------------------------------------------------
function serviceCallback(response){
	alert(response);
}

var ajax = new GLM.AJAX();
/* set new namespace for use with web service. */
ajax.setNameSpace("http://mynamespaceuri/");
ajax.callService("http://myserver.com/MyWebService.asmx", "MyMethodToCall", serviceCallback);


error handling example:
--------------------------------------------------------
/* by default the errors are alerted.  To suppress this you must redirect them. */
function myErrorHandler(error){
	alert(error);
}

var ajax = new GLM.AJAX();
ajax.onError = myErrorHandler;


Changes
6/30/2005	Added SetNameSpace, GetNameSpace methods for custom web
service namespaces.
8/21/2005	Added map to callback routines to protect against race conditions.
1/23/2006	Removed removeFrame() and used this.removeNode() instead.  Fixed firefox hourglass bug.
2/14/2006	Added support for Opera 8, Removed removeNode function from mozilla, added security checking for Mozilla SOAPCall.
8/25/2006	Made library more portable and compatible with other libraries, prefixed with GLM namespace.  Added glm-jsd documentation
		tags to source code, compressed glm-ajax using glm-jsc.  Removed all iframe code.
9/5/2006	Fixed error submitted by user, null pointer exception.
4/3/2007	Added method, async, and args to callPage method to allow for
both POST and GET requests.
4/30/2007	Fixed Firefox 2.2 bug, now compatible.
8/13/2008	Incorporated changes from Johnathan Winterflood, fixed
		ao.encode, getNameSpace() and Map.put().
