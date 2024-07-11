const { Client } = require('pg');
const fs = require('fs');

async function testPostgreSQL() {
  try {
    // secret.json 파일 읽기
    const secret = JSON.parse(fs.readFileSync('../secret.json', 'utf8'));

    // 데이터베이스 연결 정보 추출
    const postgresDatabase = secret.credentials.database;
    const postgresUser = secret.credentials.username;
    const postgresPassword = secret.credentials.password;
    const postgresHost = secret.credentials.externalHosts.split(':')[0];
    const postgresPort = secret.credentials.port;
    const postgresUri = `postgresql://${postgresUser}:${postgresPassword}@${postgresHost}:${postgresPort}/${postgresDatabase}`;

    // PostgreSQL 클라이언트 설정
    const client = new Client({
      connectionString: postgresUri
    });

    // 데이터베이스에 연결
    await client.connect();

    // 쿼리 실행
    const res = await client.query('SELECT * FROM test.TempHumi LIMIT 2');
    const rows = res.rows;
    const colnames = res.fields.map(field => field.name);

    const result = rows.map(row => {
      let obj = {};
      colnames.forEach((col, idx) => {
        obj[col] = row[col];
      });
      return obj;
    });

    // 연결 종료
    await client.end();

    return result;
  } catch (e) {
    console.error(`An error occurred: ${e.message}`);
    return { Err: `An error occurred: ${e.message}` };
  }
}

testPostgreSQL().then(result => console.log(result));
