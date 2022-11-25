SELECT YEAR(B.SALES_DATE) YEAR,MONTH(B.SALES_DATE) MONTH,GENDER,COUNT(DISTINCT A.USER_ID) USERS
FROM USER_INFO A INNER JOIN ONLINE_SALE B
ON A.USER_ID=B.USER_ID
WHERE A.GENDER IS NOT NULL
GROUP BY YEAR,MONTH,GENDER
ORDER BY YEAR,MONTH,GENDER