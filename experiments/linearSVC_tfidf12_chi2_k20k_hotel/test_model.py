from unittest import TestCase
from model import sentiment


class TestSentiment(TestCase):
    def test_sentiment_1(self):
        text = "Ăn khá ngon, bánh tráng hơi khô một tí nhưng ăn vẫn ok. Quán hơi nhỏ một tí, trang trí khá đơn giản, " \
               "phục vụ còn hơi chậm. Giá cả khá rẻ phù hợp với sinh viên, trung bình 2 bạn ăn tầm 40k hơn. "
        actual = sentiment(text)
        expected = ('AMBIENCE#GENERAL#NEUTRAL', 'FOOD#PRICE#POSITIVE', 'FOOD#QUALITY#POSITIVE', 'SERVICE#GENERAL#NEUTRAL')
        self.assertEquals(actual, expected)

    def test_sentiment_2(self):
        text = "Bánh ăn thơm và vừa miệng. Gìon rụm, ngọt nhưng không quá gắt. Đáng để thử "
        actual = sentiment(text)
        expected = ('FOOD#QUALITY#POSITIVE',)
        self.assertEquals(actual, expected)

    def test_sentiment_3(self):
        text = "ấn tg đầu tiên, quá đắt,50k cho 1 xuất cơm ntn. Là m lâu k ăn cơm, k biết giá hay cơm đắt thật k biết " \
               "nữa. Cơm chả có j đặc biệt :)k bh ăn nữa "
        actual = sentiment(text)
        expected = ('FOOD#PRICE#NEGATIVE', 'FOOD#QUALITY#POSITIVE')
        self.assertEquals(actual, expected)

    def test_sentiment_4(self):
        text = "Ăn bình thường, cho nhiều hỗn hợp quá nên ăn mau ngán. Theo mình là khá ngọt nữa. 1 đĩa chỉ có 25k " \
               "nên ko đòi hỏi gì nhiều. Mình thấy mấy phần fast food ăn ok hơn nhiều nha. 2 người tầm 80k là đủ no " \
               "rồi. "
        actual = sentiment(text)
        expected = ('FOOD#PRICE#NEUTRAL', 'FOOD#QUALITY#POSITIVE')
        self.assertEquals(actual, expected)
