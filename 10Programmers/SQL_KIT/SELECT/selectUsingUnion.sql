SELECT DATE_FORMAT(N.SALES_DATE,'%Y-%m-%d') AS SALES_DATE
    ,PRODUCT_ID,USER_ID,SALES_AMOUNT
    FROM ONLINE_SALE N
    WHERE SALES_DATE LIKE '2022-03-%'
UNION 
SELECT DATE_FORMAT(F.SALES_DATE,'%Y-%m-%d') AS SALES_DATE
    ,PRODUCT_ID,NULL as USER_ID,SALES_AMOUNT
    FROM OFFLINE_SALE F
    WHERE SALES_DATE LIKE '2022-03-%'
ORDER BY SALES_DATE,PRODUCT_ID,USER_ID