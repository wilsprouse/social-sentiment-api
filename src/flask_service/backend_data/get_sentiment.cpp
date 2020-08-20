#include <iostream>
#include <string>
#include <curl/curl.h>
using namespace std;



size_t writeFunction(void *ptr, size_t size, size_t nmemb, std::string* data) {
    data->append((char*) ptr, size * nmemb);
    return size * nmemb;
}



int main(int argc, char *argv[]) {
	cout << argv[1] <<'\n';

	//CURL *curl;

	
	curl_global_init(CURL_GLOBAL_DEFAULT);

	CURL *curl = curl_easy_init();

	if (curl) {

        	curl_easy_setopt(curl, CURLOPT_URL, "https://eresearch.fidelity.com/eresearch/evaluate/news/basicNews.jhtml?symbols=MSFT");

		curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writeFunction);

		std::string response_string;
        	std::string header_string;
        	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writeFunction);
        	curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response_string);
        	curl_easy_setopt(curl, CURLOPT_HEADERDATA, &header_string);

        	curl_easy_perform(curl);
        	cout << response_string;
        	curl_easy_cleanup(curl);
        	curl_global_cleanup();
        	curl = NULL;
	}
	return 0;
}
