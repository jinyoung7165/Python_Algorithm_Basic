SELECT a.FOOD_TYPE,a.REST_ID,a.REST_NAME,a.FAVORITES
FROM REST_INFO a JOIN (
    SELECT FOOD_TYPE, MAX(FAVORITES) AS FAVORITES
    FROM REST_INFO
    GROUP BY FOOD_TYPE) b -- 각 카테고리별 최대 FAVORITES
    ON a.FAVORITES=b.FAVORITES AND A.FOOD_TYPE = B.FOOD_TYPE
     -- b에 해당하는 칼럼만 남기기 (교집합)
ORDER BY FOOD_TYPE DESC;

SELECT FOOD_TYPE,REST_ID,REST_NAME, FAVORITES
from REST_INFO
where FAVORITES in (select max(favorites) from rest_info 
                   group by food_type)
group by FOOD_TYPE order by FOOD_TYPE desc