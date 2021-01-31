CREATE TABLE CHARTER_OFFICER_BUSINESS (
    FILING_NUM TEXT,
    LAYOUT_CODE TEXT,
    ADDRESS1 TEXT,
    ADDRESS2 TEXT,
    CITY TEXT,
    STATE TEXT,
    ZIP_CODE TEXT,
    ZIP_EXTENSION TEXT,
    COUNTRY TEXT,
    OFFICER_ID NUMERIC,
    OFFICER_TITLE TEXT,
    BUSINESS_NAME TEXT
);
CREATE INDEX ON CHARTER_OFFICER_BUSINESS(FILING_NUM);