#include <iostream>
#include <vector>
#include <string>

struct WeatherInfo {
    std::string main;
    double temp;
    std::string description;
};

struct HealthData {
    double heartRate;
    double sleepHours;
    int age;
    std::string goal;
};

std::string recommendWorkout(double heartRate, double sleepHours, int age, const std::string& goal) {
    std::string recommendation;

    if (sleepHours < 6) {
        recommendation = "수면이 부족합니다. 가벼운 스트레칭과 짧은 산책을 추천합니다.";
    } else if (heartRate > 90) {
        recommendation = "심박수가 높으니 무리한 운동 대신 요가, 스트레칭 등 저강도 운동을 하세요.";
    } else if (goal == "다이어트" || goal == "체중감량") {
        recommendation = "유산소 운동(런닝, 사이클) 30분과 가벼운 근력운동을 추천합니다.";
    } else if (goal == "근육증가") {
        recommendation = "근력운동(스쿼트, 푸쉬업 등)을 40분 이상 하시고, 유산소는 가볍게 하세요.";
    } else if (goal == "건강관리") {
        recommendation = "걷기, 조깅, 스트레칭 등 전신을 활용한 운동을 매일 30분 이상 하세요.";
    } else {
        recommendation = "가벼운 운동과 스트레칭으로 시작해보세요.";
    }
    return recommendation;
}

std::string getWeatherComment(const WeatherInfo& w) {
    if (w.main == "Rain") {
        return "오늘은 비가 오니 실내운동을 권장합니다.";
    } else if (w.temp >= 30.0) {
        return "기온이 높으니 운동 전후 수분 보충에 신경쓰세요.";
    } else if (w.temp <= 0.0) {
        return "날씨가 추우니 충분히 준비운동을 하시고, 실내운동도 고려하세요.";
    } else if (w.main == "Clear") {
        return "날씨가 맑으니 야외운동도 좋겠습니다!";
    }
    return "";
}

int main() {
    // [1] 고정 날씨 샘플 10개
    std::vector<WeatherInfo> weatherSamples = {
        {"Clear", 23.5, "clear sky"},
        {"Rain", 17.2, "light rain"},
        {"Clouds", 20.1, "scattered clouds"},
        {"Snow", -2.3, "light snow"},
        {"Clear", 31.4, "sunny"},
        {"Rain", 14.9, "heavy rain"},
        {"Clouds", 27.0, "overcast clouds"},
        {"Clear", 8.6, "cold and clear"},
        {"Drizzle", 18.7, "drizzle"},
        {"Thunderstorm", 22.5, "thunderstorm with rain"}
    };

    // [2] 건강 샘플 데이터(고정 샘플)
    std::vector<HealthData> sampleData = {
        {76, 5.2, 22, "다이어트"},
        {88, 6.0, 27, "근육증가"},
        {65, 7.5, 31, "건강관리"},
        {95, 4.8, 19, "다이어트"},
        {72, 6.9, 41, "건강관리"},
        {82, 5.6, 35, "근육증가"},
        {60, 8.0, 24, "다이어트"},
        {99, 5.0, 29, "건강관리"},
        {71, 7.2, 33, "근육증가"},
        {78, 6.4, 38, "건강관리"},
        {85, 5.8, 45, "다이어트"},
        {67, 7.8, 26, "건강관리"},
        {62, 6.7, 21, "근육증가"},
        {93, 4.9, 36, "다이어트"},
        {80, 6.1, 30, "건강관리"},
        {69, 7.0, 28, "근육증가"},
        {75, 7.3, 23, "건강관리"},
        {90, 5.5, 34, "근육증가"},
        {64, 8.1, 20, "다이어트"},
        {87, 5.7, 40, "건강관리"}
    };

    // [3] 각 날씨 샘플에 대해 20개 건강 데이터 적용
    for (size_t widx = 0; widx < weatherSamples.size(); ++widx) {
        const auto& weather = weatherSamples[widx];
        std::cout << "\n===================================================\n";
        std::cout << "[날씨 샘플 #" << (widx + 1) << "]\n";
        std::cout << "  상태: " << weather.main << " (" << weather.description << ")\n";
        std::cout << "  온도: " << weather.temp << "도\n";
        std::cout << getWeatherComment(weather) << "\n";
        std::cout << "---------------------------------------------------\n";
        for (size_t i = 0; i < sampleData.size(); ++i) {
            const auto& d = sampleData[i];
            std::cout << "샘플 #" << (i+1) << ":\n";
            std::cout << "  심박수: " << d.heartRate << " bpm\n";
            std::cout << "  수면시간: " << d.sleepHours << " 시간\n";
            std::cout << "  나이: " << d.age << "세\n";
            std::cout << "  운동 목표: " << d.goal << "\n";
            std::cout << "  맞춤 운동 추천: " << recommendWorkout(d.heartRate, d.sleepHours, d.age, d.goal) << "\n";
            std::cout << "  [날씨 코멘트] " << getWeatherComment(weather) << "\n";
            std::cout << "---------------------------------------------------\n";
        }
    }
    return 0;
}
