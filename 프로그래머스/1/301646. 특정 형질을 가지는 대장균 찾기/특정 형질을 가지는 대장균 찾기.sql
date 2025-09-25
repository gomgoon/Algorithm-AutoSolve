SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0      -- 형질 2 없음
  AND (GENOTYPE & 5) > 0;     -- 형질 1 또는 3 있음 (5 = 1|4)
