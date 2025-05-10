function getRecommendation() {
  const mood = document.getElementById('moodInput').value;
  const calories = document.getElementById('calories').value;
  const sleepH = document.getElementById('sleepHours').value;
  const sleepM = document.getElementById('sleepMinutes').value;

  const totalSleep = parseInt(sleepH) * 60 + parseInt(sleepM);

  const payload = {
    mood: mood,
    calories: parseInt(calories),
    sleepMinutes: totalSleep
  };

  fetch('http://localhost:5000/recommend', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById('recommendationResult').innerText =
      `추천 운동: ${data.recommendation} (${data.duration}분)`;
  })
  .catch(err => {
    console.error('에러 발생:', err);
    document.getElementById('recommendationResult').innerText = '추천을 가져오는 데 실패했어요.';
  });
}