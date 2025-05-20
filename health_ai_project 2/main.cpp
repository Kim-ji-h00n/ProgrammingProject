#define CROW_MAIN
#define CROW_USE_ASIO
#define _ENABLE_EXTENDED_ALIGNED_STORAGE

#include "crow_all.h"
#include <string>

std::string recommendWorkout(const std::string& goal) {
    if (goal == "근육") return "상체 + 하체 웨이트 루틴 추천";
    if (goal == "다이어트") return "유산소 + 코어 운동 추천";
    return "스트레칭 및 가벼운 운동 추천";
}

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/")([] {
        crow::response res;
        res.code = 200;
        res.set_header("Content-Type", "text/html; charset=utf-8");

        res.body = R"(
            <!DOCTYPE html>
            <html lang="ko">
            <head>
                <meta charset="UTF-8">
                <title>운동 추천</title>
            </head>
            <body>
                <h1>운동 목표를 입력하세요</h1>
                <form action='/recommend' method='post'>
                    <input name='goal' placeholder='근육 or 다이어트'/>
                    <input type='submit' value='추천 받기'/>
                </form>
            </body>
            </html>
        )";
        return res;
    });

    CROW_ROUTE(app, "/recommend").methods("POST"_method)([](const crow::request& req) {
        auto goal = req.url_params.get("goal");
        std::string result = recommendWorkout(goal ? goal : "default");

        std::string html = R"(
            <!DOCTYPE html>
            <html lang="ko">
            <head>
                <meta charset="UTF-8">
                <title>운동 추천 결과</title>
            </head>
            <body>
                <h2>추천 루틴:</h2>
                <p>)" + result + R"(</p>
            </body>
            </html>
        )";

        crow::response res;
        res.code = 200;
        res.set_header("Content-Type", "text/html; charset=utf-8");
        res.body = html;

        return res;
    });

    app.port(18080).multithreaded().run();
}