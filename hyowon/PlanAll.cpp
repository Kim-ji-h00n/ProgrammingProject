#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include "nlohmann/json.hpp"

using namespace std;
using json = nlohmann::json;

struct HealthStatus {
    string name;
    float sleepHours;
    int heartRate;
    int stressLevel;
};
struct WorkoutLog {
    string date, user, intensity;
    vector<string> exercises;
    int duration = 0;
    json to_json() const {
        return { {"date",date}, {"user",user}, {"intensity",intensity}, {"exercises",exercises}, {"duration",duration} };
    }
};
string getTodayDate() {
    time_t now = time(nullptr); tm t{}; localtime_s(&t, &now);
    char buf[11]; strftime(buf, sizeof(buf), "%Y-%m-%d", &t); return string(buf);
}
vector<HealthStatus> loadHealthDataset(const string& filename) {
    ifstream file(filename); json j; file >> j;
    vector<HealthStatus> data;
    for(const auto& item: j) {
        HealthStatus hs;
        hs.name = item.value("name","");
        hs.sleepHours = item.value("sleepHours",0.0f);
        hs.heartRate = item.value("heartRate",0);
        hs.stressLevel = item.value("stressLevel",0);
        data.push_back(hs);
    } return data;
}
WorkoutLog generateWorkout(const HealthStatus& hs) {
    WorkoutLog log; log.date=getTodayDate(); log.user=hs.name;
    if(hs.sleepHours<5.0f||hs.stressLevel>70) { log.intensity="약함"; log.exercises={"스트레칭","요가","걷기"}; log.duration=20; }
    else if(hs.heartRate>90||hs.sleepHours<6.0f){ log.intensity="보통"; log.exercises={"런지","푸쉬업","버피"}; log.duration=30; }
    else{ log.intensity="강함"; log.exercises={"스쿼트","데드리프트","벤치프레스"}; log.duration=40; }
    return log;
}
void saveWorkout(const WorkoutLog& log, const string& filename="workout_log.json") {
    json data = json::array();
    ifstream inFile(filename); if(inFile.is_open()) { inFile >> data; inFile.close();}
    data.push_back(log.to_json());
    ofstream outFile(filename); outFile << data.dump(4); outFile.close();
}
int main() {
    vector<HealthStatus> users = loadHealthDataset("health_dataset.json");
    for(const auto& user: users) {
        WorkoutLog log = generateWorkout(user);
        saveWorkout(log);
        cout << "사용자: " << log.user << " | 강도: " << log.intensity << " | 운동: ";
        for(const auto& ex: log.exercises) cout << ex << " ";
        cout << "| 시간: " << log.duration << "분n";
    }
    cout << "n✅ 모든 운동 추천 및 기록 저장이 완료되었습니다.n";
    return 0;
}
