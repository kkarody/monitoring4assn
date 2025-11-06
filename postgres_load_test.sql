
-- 1. Create test table (only once)
CREATE TABLE IF NOT EXISTS test_data (
    id SERIAL PRIMARY KEY,
    txt TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- 2. Main activity block (insert, update, delete, select)
INSERT INTO test_data (txt)
SELECT md5(random()::text)
FROM generate_series(1, 5000);

UPDATE test_data
SET txt = md5(random()::text)
WHERE id % 10 = 0;

DELETE FROM test_data
WHERE id % 15 = 0;

SELECT COUNT(*) FROM test_data;
SELECT AVG(length(txt)) FROM test_data;
SELECT * FROM test_data ORDER BY RANDOM() LIMIT 100;

-- 3. Automatic loop (generate continuous activity)
DO $$
BEGIN
  FOR i IN 1..20 LOOP
    INSERT INTO test_data (txt)
    SELECT md5(random()::text) FROM generate_series(1, 1000);

    UPDATE test_data
    SET txt = md5(random()::text)
    WHERE id % 25 = 0;

    DELETE FROM test_data WHERE id % 100 = 0;

    PERFORM pg_sleep(5); -- 5 sec pause between cycles
  END LOOP;
END $$;

