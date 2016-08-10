//some needed global variables
var sse_tag_id        = null;
var sse_event_source  = null;
var next_operation    = null;
var event_run         = false;
var event_msg         = null;
//this function is to change the active menu
function sse_updater(tag_id,stream_url)
{
	//close the old SSE stream
	if (sse_tag_id != null)
	{
	   sse_event_source.close();
	}
	//open a new SSE stream
	sseUpdateByID(tag_id,stream_url);
}

//Server Sent Events update div function
function sseUpdateByID(tag_id,source)
{
	var eventSource = new EventSource(source);
  console.log(tag_id)
	sse_tag_id  = tag_id;
	sse_event_source  = eventSource;
	eventSource.addEventListener("message", sseUpdateDivOperation);
  // add to close the stream if load = 100%
  console.log("after adding the listner");
}
function sseUpdateDivOperation()
{
	event_run = true;
  if (isNaN(event.data))
  {
    sse_event_source.close();
		event_msg = event.data;
		event_run = false;
  }
	else
	{
		$bar = $(sse_tag_id);
		$bar.width(event.data+"%");
	}
}
