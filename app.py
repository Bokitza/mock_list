customers = [
  {"first_name": "תמר", "last_name": "כהן", "age": 46, "burgers": 64, "fries": 52, "ice_cream": 94, "club": true},
  {"first_name": "עומר", "last_name": "לוי", "age": 99, "burgers": 77, "fries": 90, "ice_cream": 87, "club": false},
  {"first_name": "אור", "last_name": "רוזן", "age": 20, "burgers": 18, "fries": 7, "ice_cream": 49, "club": true},
  {"first_name": "יואב", "last_name": "פרידמן", "age": 71, "burgers": 50, "fries": 21, "ice_cream": 2, "club": true},
  {"first_name": "שחר", "last_name": "יעקובוביץ", "age": 56, "burgers": 25, "fries": 63, "ice_cream": 100, "club": false},
  {"first_name": "דפנה", "last_name": "אביב", "age": 86, "burgers": 53, "fries": 83, "ice_cream": 44, "club": true},
  {"first_name": "נעם", "last_name": "ברק", "age": 78, "burgers": 60, "fries": 73, "ice_cream": 8, "club": true},
  {"first_name": "מעיין", "last_name": "שטרן", "age": 44, "burgers": 81, "fries": 94, "ice_cream": 61, "club": false},
  {"first_name": "דנה", "last_name": "צור", "age": 88, "burgers": 5, "fries": 45, "ice_cream": 9, "club": false},
  {"first_name": "שיר", "last_name": "מזרחי", "age": 39, "burgers": 7, "fries": 98, "ice_cream": 39, "club": false},
  {"first_name": "אליאנה", "last_name": "ארבל", "age": 47, "burgers": 67, "fries": 15, "ice_cream": 4, "club": true},
  {"first_name": "אביה", "last_name": "רון", "age": 89, "burgers": 90, "fries": 26, "ice_cream": 22, "club": false},
  {"first_name": "רז", "last_name": "גולן", "age": 28, "burgers": 71, "fries": 61, "ice_cream": 24, "club": false},
  {"first_name": "גיא", "last_name": "בן-דוד", "age": 62, "burgers": 3, "fries": 11, "ice_cream": 16, "club": true},
  {"first_name": "רותם", "last_name": "כהן", "age": 76, "burgers": 34, "fries": 41, "ice_cream": 32, "club": false},
  {"first_name": "נעמה", "last_name": "אביטן", "age": 37, "burgers": 88, "fries": 76, "ice_cream": 13, "club": false},
  {"first_name": "אדם", "last_name": "אלקיים", "age": 66, "burgers": 48, "fries": 20, "ice_cream": 31, "club": true},
  {"first_name": "ניצן", "last_name": "דרור", "age": 79, "burgers": 85, "fries": 30, "ice_cream": 53, "club": false},
  {"first_name": "אלה", "last_name": "ביטון", "age": 53, "burgers": 26, "fries": 64, "ice_cream": 77, "club": false},
  {"first_name": "רוני", "last_name": "נוימן", "age": 94, "burgers": 98, "fries": 69, "ice_cream": 95, "club": false},
  {"first_name": "שירה", "last_name": "מלכה", "age": 59, "burgers": 42, "fries": 6, "ice_cream": 90, "club": true},
  {"first_name": "מאיה", "last_name": "זיו", "age": 22, "burgers": 46, "fries": 93, "ice_cream": 70, "club": true},
  {"first_name": "אבישג", "last_name": "קרני", "age": 67, "burgers": 99, "fries": 18, "ice_cream": 64, "club": true},
  {"first_name": "יובל", "last_name": "קושניר", "age": 84, "burgers": 74, "fries": 23, "ice_cream": 55, "club": true},
  {"first_name": "אייל", "last_name": "שלו", "age": 90, "burgers": 21, "fries": 12, "ice_cream": 29, "club": false},
  {"first_name": "עמית", "last_name": "זילברמן", "age": 85, "burgers": 17, "fries": 74, "ice_cream": 58, "club": false},
  {"first_name": "יונתן", "last_name": "מימון", "age": 41, "burgers": 95, "fries": 46, "ice_cream": 89, "club": false},
  {"first_name": "שני", "last_name": "נחום", "age": 83, "burgers": 6, "fries": 10, "ice_cream": 62, "club": false},
  {"first_name": "שלי", "last_name": "ישראלי", "age": 32, "burgers": 65, "fries": 17, "ice_cream": 30, "club": true},
  {"first_name": "אפרת", "last_name": "גל", "age": 25, "burgers": 57, "fries": 48, "ice_cream": 6, "club": true},
  {"first_name": "אורי", "last_name": "עזר", "age": 27, "burgers": 12, "fries": 28, "ice_cream": 63, "club": false},
  {"first_name": "שירה", "last_name": "רז", "age": 95, "burgers": 36, "fries": 1, "ice_cream": 99, "club": true},
  {"first_name": "יואב", "last_name": "כהן", "age": 61, "burgers": 38, "fries": 97, "ice_cream": 11, "club": false},
  {"first_name": "אביב", "last_name": "מאור", "age": 54, "burgers": 13, "fries": 22, "ice_cream": 85, "club": true},
  {"first_name": "דניאל", "last_name": "שמואלי", "age": 31, "burgers": 35, "fries": 5, "ice_cream": 33, "club": false},
  {"first_name": "איתן", "last_name": "כהנא", "age": 74, "burgers": 59, "fries": 14, "ice_cream": 28, "club": true},
  {"first_name": "ליאן", "last_name": "רוטמן", "age": 64, "burgers": 33, "fries": 84, "ice_cream": 56, "club": true},
  {"first_name": "אדר", "last_name": "אלון", "age": 55, "burgers": 31, "fries": 99, "ice_cream": 12, "club": true},
  {"first_name": "שחר", "last_name": "שמיר", "age": 26, "burgers": 61, "fries": 56, "ice_cream": 18, "club": false},
  {"first_name": "עידו", "last_name": "פיין", "age": 92, "burgers": 24, "fries": 2, "ice_cream": 84, "club": false},
  {"first_name": "לירון", "last_name": "וייס", "age": 60, "burgers": 16, "fries": 75, "ice_cream": 93, "club": true},
  {"first_name": "אורי", "last_name": "פרץ", "age": 49, "burgers": 20, "fries": 54, "ice_cream": 45, "club": false},
  {"first_name": "מיה", "last_name": "נגר", "age": 30, "burgers": 0, "fries": 0, "ice_cream": 14, "club": true},
  {"first_name": "אור", "last_name": "הראל", "age": 52, "burgers": 10, "fries": 9, "ice_cream": 1, "club": false},
  {"first_name": "יעל", "last_name": "בן חורין", "age": 40, "burgers": 0, "fries": 0, "ice_cream": 59, "club": false},
  {"first_name": "אייל", "last_name": "חזן", "age": 34, "burgers": 14, "fries": 16, "ice_cream": 36, "club": true},
  {"first_name": "רוני", "last_name": "כץ", "age": 24, "burgers": 79, "fries": 38, "ice_cream": 65, "club": false},
  {"first_name": "תהל", "last_name": "שלם", "age": 43, "burgers": 2, "fries": 42, "ice_cream": 3, "club": false},
  {"first_name": "אלון", "last_name": "זמיר", "age": 68, "burgers": 41, "fries": 8, "ice_cream": 91, "club": true},
  {"first_name": "אדם", "last_name": "גולדשטיין", "age": 87, "burgers": 0, "fries": 0, "ice_cream": 79, "club": true}
]

# כמה המבורגרים נקנו סך הכל בשנה האחרונה?


# כמה צ'יפס ננה סך הכל בשנה האחרונה?


# כמה חברי מועדון נרשמו בשנה האחרונה?


# מה אחוז חברי המועדון מסך הלקוחות?


# מה הגיל הממוצע של הלקוחות שלנו?


# כמה אנשים קנו רק קינוח (בלי צ'יפס או המבורגר)?


# תדפיסו את השם המלא של כל האנשים מעל גיל 50 שקנו בחנות בשנה האחרונה


# בונוס- האם בעיקר ילדים קונים גלידות? הוכיחו בעזרת מילים וקוד

# מי הלקוח שקנה הכי הרבה המבורגרים?


#מי הלקוח שקנה הכי הרבה דברים סך הכל? (המבורגר+צ'יפס+גלידה) 


# 
