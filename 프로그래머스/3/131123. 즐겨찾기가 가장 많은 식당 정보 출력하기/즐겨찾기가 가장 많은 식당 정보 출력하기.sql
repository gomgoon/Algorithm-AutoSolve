-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO R
WHERE (SELECT MAX(FAVORITES) FROM REST_INFO E WHERE R.FOOD_TYPE = E.FOOD_TYPE) = FAVORITES
ORDER BY FOOD_TYPE DESC;