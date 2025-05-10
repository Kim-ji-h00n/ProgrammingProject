#include <iostream>
#include <string>
#include <sstream>
#include <curl/curl.h>

std::string responseBuffer;

size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    size_t totalSize = size * nmemb;
    responseBuffer.append((char*)contents, totalSize);
    return totalSize;
}

int main() {
    std::string mood;
    int calories, sleepHours, sleepMinutes;

    std::cout << "기분을 입력하세요: ";
    std::getline(std::cin, mood);
    std::cout << "칼로리 소비량을 입력하세요 (kcal): ";
    std::cin >> calories;
    std::cout << "수면 시간 (시간): ";
    std::cin >> sleepHours;
    std::cout << "수면 시간 (분): ";
    std::cin >> sleepMinutes;

    int totalSleep = sleepHours * 60 + sleepMinutes;

    std::stringstream jsonData;
    jsonData << "{";
    jsonData << "\"mood\":\"" << mood << "\",";
    jsonData << "\"calories\":" << calories << ",";
    jsonData << "\"sleepMinutes\":" << totalSleep;
    jsonData << "}";

    CURL* curl;
    CURLcode res;

    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();

    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, "http://localhost:5000/recommend");
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, jsonData.str().c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);

        struct curl_slist* headers = NULL;
        headers = curl_slist_append(headers, "Content-Type: application/json");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        res = curl_easy_perform(curl);

        if(res != CURLE_OK)
            std::cerr << "요청 실패: " << curl_easy_strerror(res) << std::endl;
        else
            std::cout << "운동 추천 결과: " << responseBuffer << std::endl;

        curl_easy_cleanup(curl);
        curl_slist_free_all(headers);
    }

    curl_global_cleanup();
    return 0;
}