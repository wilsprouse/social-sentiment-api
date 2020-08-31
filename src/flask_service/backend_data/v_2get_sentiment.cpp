#include <libxml/tree.h>
#include <libxml/HTMLparser.h>
#include <libxml++/libxml++.h>
 
#include <curlpp/cURLpp.hpp>
#include <curlpp/Easy.hpp>
#include <curlpp/Options.hpp>
 
#include <iostream>
#include <string>
 
#define HEADER_ACCEPT "Accept:text/html,application/xhtml+xml,application/xml"
#define HEADER_USER_AGENT "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.70 Safari/537.17"
 
int main() {
    std::string url = "http://www.iplocation.net/";
    curlpp::Easy request;
 
    // Specify the URL
    request.setOpt(curlpp::options::Url(url));
 
    // Specify some headers
    std::list<std::string> headers;
    headers.push_back(HEADER_ACCEPT);
    headers.push_back(HEADER_USER_AGENT);
    request.setOpt(new curlpp::options::HttpHeader(headers));
    request.setOpt(new curlpp::options::FollowLocation(true));
 
    // Configure curlpp to use stream
    std::ostringstream responseStream;
    curlpp::options::WriteStream streamWriter(&responseStream);
    request.setOpt(streamWriter);
 
    // Collect response
    request.perform();
    std::string re = responseStream.str();
 
    // Parse HTML and create a DOM tree
    xmlDoc* doc = htmlReadDoc((xmlChar*)re.c_str(), NULL, NULL, HTML_PARSE_RECOVER | HTML_PARSE_NOERROR | HTML_PARSE_NOWARNING);
 
    //std::cout << *doc << std::endl;
    // Encapsulate raw libxml document in a libxml++ wrapper
    xmlNode* r = xmlDocGetRootElement(doc);
    xmlpp::Element* root = new xmlpp::Element(r);
    std::cout << *root << std::endl;
 
    // Grab the IP address
    std::string xpath = "//*[@id=\"locator\"]/p[1]/b/font/text()";
    //auto elements = root->find(xpath);
    //std::cout << "Your IP address is:" << std::endl;
    //std::cout << dynamic_cast<xmlpp::ContentNode*>(elements[0])->get_content() << std::endl;
 
    delete root;
    xmlFreeDoc(doc);
 
    return 0;
}
