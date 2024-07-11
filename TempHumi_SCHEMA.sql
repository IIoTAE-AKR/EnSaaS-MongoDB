-- test 스키마 내에 TempHumi 테이블 생성
CREATE TABLE test.TempHumi (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deviceId INT NOT NULL,
    temp FLOAT NOT NULL,
    humi FLOAT NOT NULL
);

-- 예시 데이터 삽입
INSERT INTO test.TempHumi (deviceId, temp, humi) VALUES 
    (1, 25.5, 60.2),
    (2, 26.0, 58.8),
    (3, 26.5, 57.3),
    (4, 27.0, 55.9);