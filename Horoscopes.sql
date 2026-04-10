-----------------------------------------------------------------------------------------------------------------------
-- Database to hold zodiac signs and user birthdays
-----------------------------------------------------------------------------------------------------------------------
PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS ZodiacSigns;
DROP TABLE IF EXISTS Birthdays;
DROP TABLE IF EXISTS DailyHoroscope;
DROP TABLE IF EXISTS UserDailyHoroscope;

CREATE TABLE ZodiacSigns (
    sign TEXT,
    startDate CHECK ( startDate IS strftime('%m%d', 'now')),
    endDate CHECK (endDate IS strftime('%m%d', 'now')),
    CONSTRAINT zodiac_pk PRIMARY KEY (sign)
);

CREATE TABLE Birthdays (
    userId INTEGER,
    username TEXT,
    userBirthday TEXT,
    zodiacSign TEXT,
    CONSTRAINT birthday_pk PRIMARY KEY (userId),
    CONSTRAINT birthday_fk FOREIGN KEY (zodiacSign)
        REFERENCES ZodiacSigns (sign)
);

-- Maybe do a table for each Zodiac sign, so we don't have a table that is overwhelmed with data
CREATE TABLE DailyHoroscope (
    horoscopeId INTEGER,
    horoscopeDate TEXT CHECK (strftime('%m/%d/%y', 'now')),
    horoscopeSign TEXT,
    horoscopeText TEXT,
    CONSTRAINT horoscope_pk PRIMARY KEY (horoscopeId),
    CONSTRAINT horoscope_fk FOREIGN KEY (horoscopeSign)
        REFERENCES ZodiacSigns (sign)
);

CREATE TABLE UserDailyHoroscope (
    userId INTEGER,
    zodiacSign TEXT,
    horoscopeDate TEXT CHECK (strftime('%m/%d/%y', 'now')),
    horoscopeText TEXT,
    CONSTRAINT userhoroscope_pk PRIMARY KEY (userId),
    CONSTRAINT userhoroscopesign_fk FOREIGN KEY (zodiacSign) REFERENCES ZodiacSigns (sign),
    CONSTRAINT userhoroscopedate_fk FOREIGN KEY (horoscopeDate) REFERENCES DailyHoroscope (horoscopeDate),
    CONSTRAINT userhoroscopetext_fk FOREIGN KEY (horoscopeText) REFERENCES DailyHoroscope (horoscopeText)

)

INSERT INTO ZodiacSigns (sign, startDate, endDate)
    VALUES
        ('Capricorn', '1222','0119'),
        ('Aquarius', '0120','0218'),
        ('Pisces','0219','0320'),
        ('Aries','0321','0419'),
        ('Taurus','0420','0520'),
        ('Gemini','0521','0621'),
        ('Cancer','0622','0722'),
        ('Leo','0723','0822'),
        ('Virgo','0823','0922'),
        ('Libra','0923','1023'),
        ('Scorpio','1024','1121'),
        ('Sagittarius','1122','1221');