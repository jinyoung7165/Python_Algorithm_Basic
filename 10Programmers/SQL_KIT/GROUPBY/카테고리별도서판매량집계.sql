SELECT
B.CATEGORY,
SUM(S.SALES) AS TOTAL_SALES
FROM BOOK B
LEFT JOIN BOOK_SALES S ON B.BOOK_ID = S.BOOK_ID
WHERE MONTH(S.SALES_DATE) = 1
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY ASC