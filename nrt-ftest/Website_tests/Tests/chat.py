import unittest
from Website_tests.Pages.ChatPage import ChatPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class ChatTest(unittest.TestCase):
    """
    Classe ChatTest.

    Teste les différents élements de la fonctionnalité de chat.
    """
    @classmethod
    def setUpClass(cls):
        """Charge le drive Chrome."""
        options = webdriver.ChromeOptions()

        # Enable when certificate bugs
        # options.add_argument('--ignore-certificate-errors')

        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        cls.url = "https://www.kwili.fr/landing"

    def test_chat(self):
        """
        Teste le chat widget.
        """
        self.driver.get(self.url)
        chat = ChatPage(self.driver)

        chat.click_chat_widget()
        chat.write_msg("J'ai mal")
        chat.write_msg("au pied")
        chat.write_msg("3")
        chat.write_msg("2 jours")
        chat.write_msg("oui")
        chat.write_msg("oui")
        chat.write_msg("184 cm")
        chat.write_msg("66 kg")
        chat.write_msg("non")
        chat.write_msg("Poils de chats")
        chat.write_msg("0")
        chat.write_msg("oui")
        sleep(3)

    @classmethod
    def tearDownClass(cls):
        """Ferme le driver."""
        cls.driver.close()
        cls.driver.quit()
