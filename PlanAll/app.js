const express = require('express');
const session = require('express-session');
const bcrypt = require('bcrypt');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const app = express();
const db = new sqlite3.Database('./db/planall.db');

app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: true }));
app.use(session({
    secret: 'planall_secret',
    resave: false,
    saveUninitialized: false
}));

// DB 초기화 (최초 1회만 실행)
db.serialize(() => {
    db.run(`CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )`);
    db.run(`CREATE TABLE IF NOT EXISTS health (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        heart_rate INTEGER,
        sleep_hours REAL,
        date TEXT
    )`);
});

// 회원가입
app.get('/register', (req, res) => {
    res.render('register');
});
app.post('/register', async (req, res) => {
    const { username, password } = req.body;
    const hash = await bcrypt.hash(password, 10);
    db.run('INSERT INTO users (username, password) VALUES (?, ?)', [username, hash], err => {
        if (err) return res.send('이미 존재하는 아이디입니다.');
        res.redirect('/login');
    });
});

// 로그인
app.get('/login', (req, res) => res.render('login'));
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    db.get('SELECT * FROM users WHERE username = ?', [username], async (err, user) => {
        if (!user) return res.send('아이디/비번 확인');
        const match = await bcrypt.compare(password, user.password);
        if (!match) return res.send('아이디/비번 확인');
        req.session.user = user;
        res.redirect('/dashboard');
    });
});

// 운동 데이터 기록
app.get('/dashboard', (req, res) => {
    if (!req.session.user) return res.redirect('/login');
    db.all('SELECT * FROM health WHERE user_id = ?', [req.session.user.id], (err, healths) => {
        res.render('dashboard', { user: req.session.user, healths });
    });
});
app.post('/dashboard', (req, res) => {
    const { heart_rate, sleep_hours } = req.body;
    if (!req.session.user) return res.redirect('/login');
    db.run('INSERT INTO health (user_id, heart_rate, sleep_hours, date) VALUES (?, ?, ?, DATE("now"))',
        [req.session.user.id, heart_rate, sleep_hours],
        err => res.redirect('/dashboard')
    );
});

// 로그아웃
app.get('/logout', (req, res) => {
    req.session.destroy(() => res.redirect('/login'));
});

// 서버 시작
app.listen(3000, () => {
    console.log('http://localhost:3000');
});
