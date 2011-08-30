Code Style in Homeideas
====

Semantic exception 
----

    // return throw RunTimeException("RunTimeException")
    return throw RunTimeException("no argument in url " + url )
    
Get rid of useless blank line
----

Class declaration
----

    # Const
    # Property
    # pulic Method
    # private Method
    
Const variant as a parameter, don't hard code 
----

    // def abc(){return CONST_VARIANT}
    def method(var){return var}
    method(CONST_VARIANT)

Use generic, not if/else or switch/case    
----

Dispatcher

    public class RequestUriDispatcher<Info> {
        private UrlPathHelper pathHelper = new UrlPathHelper();
        private PathMatcher matcher = new AntPathMatcher();
        
        private Map<String, Function<HttpServletRequest, Info>> functionMap = new HashMap<String, Function<HttpServletRequest, Info>>();
        public void registerHandler(String template, Function<HttpServletRequest, Info> transformer) {
            this.functionMap.put(template, transformer);
        }
        public Info dispatch(HttpServletRequest request) {
            String pathForRequest = pathHelper.getLookupPathForRequest(request);
        
            for (String template : functionMap.keySet()) {
                if (matcher.match(template, pathForRequest)) {
                    return this.functionMap.get(template).apply(request);
                }
            }

            throw new IllegalArgumentException("unknown request:" + pathForRequest);
        }
    }


    RequestUriDispatcher<OmnitureInfo> dispatcher = new RequestUriDispatcher<OmnitureInfo>();
    dispatcher.registerHandler(UriHelper.SPACE_URI_TEMPLATE, new Function<HttpServletRequest, OmnitureInfo>() {
        @Override
        public OmnitureInfo apply(HttpServletRequest request) {
            return fromSpaceRequest(request);
        }
    });

Test on handling exception
----
    
    @Test(expected = IllegalArgumentException.class)
    public void should_throw_exception_for_incorrect_results_request(){
        request.setRequestURI("/hi/results-/list-1");
        request.setContextPath("/hi");

        analyzer.fromRequest(request);
    }

Presenter should be simple and non-status
----

In the interceptor, presenter should be non-status, use a service class instead of presenter.

Presenter and Form should be split
----

Presenter is show, Form is for data save, controller use service to validate form, then render to presenter.

Naming
----
Java createForm isValid
ruby create_form has_content?
html/css class="disabled"

