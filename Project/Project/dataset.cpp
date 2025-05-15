#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "json.hpp"

using json = nlohmann::json;
using namespace std;

struct HealthStatus {
    string name;
    float sleepHours;
    int heartRate;
    int stressLevel;

    void printRecommendation() const {
        cout << "�� �����: " << name << endl;
        cout << "  - ����: " << sleepHours << "�ð� | �ɹڼ�: " << heartRate << "bpm | ��Ʈ����: " << stressLevel << endl;

        if (sleepHours < 5 || stressLevel > 70) {
            cout << "  �� � ����: ����" << endl;
            cout << "  �� ��õ �: ��Ʈ��Ī, �䰡, ������ �ȱ�" << endl;
        }
        else if (heartRate > 90 || sleepHours < 6) {
            cout << "  �� � ����: ����" << endl;
            cout << "  �� ��õ �: ����, Ǫ����, ���� ����Ʈ" << endl;
        }
        else {
            cout << "  �� � ����: ����" << endl;
            cout << "  �� ��õ �: ����Ʈ, ��ġ������, ���帮��Ʈ" << endl;
        }

        cout << "-------------------------------\n";
    }
};

vector<HealthStatus> loadHealthDataset(const string& filename) {
    ifstream file(filename);
    json data;
    file >> data;

    vector<HealthStatus> result;

    for (const auto& person : data) {
        HealthStatus hs;
        hs.name = person["name"];
        hs.sleepHours = person["sleepHours"];
        hs.heartRate = person["heartRate"];
        hs.stressLevel = person["stressLevel"];
        result.push_back(hs);
    }

    return result;
}

int main() {
    vector<HealthStatus> users = loadHealthDataset("health_dataset.json");

    for (const auto& user : users) {
        user.printRecommendation();
    }

    return 0;
}