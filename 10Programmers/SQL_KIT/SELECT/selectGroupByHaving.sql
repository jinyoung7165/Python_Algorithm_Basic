SELECT USER_ID,PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID,PRODUCT_ID
HAVING COUNT(ONLINE_SALE_ID) > 1 --두번이상 같은 상품 산 유저 행 count
ORDER BY USER_ID,PRODUCT_ID DESC;