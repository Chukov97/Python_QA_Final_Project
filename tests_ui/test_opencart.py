import allure
import pytest

from page_objects.CatalogPage import CatalogPage
from page_objects.MainPage import MainPage
from page_objects.RegisterPage import RegisterPage


class TestOpencart:

    @allure.title("Elements on main page")
    def test_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        assert main_page.count_heading_links() == 7
        search_placeholder = main_page.search_placeholder()
        assert search_placeholder == "Searc"

    @allure.title("Change currency om main page")
    def test_switch_currency(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.change_currency("EUR")
        assert main_page.CURRENCY["EUR"] == main_page.current_sign_currency

    @allure.title("Elements on catalog page")
    def test_catalog_page(self, driver):
        catalog_page = CatalogPage(driver)
        catalog_page.open_laptop_page()
        assert driver.title == "Laptops & Notebooks"
        assert catalog_page.count_product_cards == 5
        catalog_page.sort_products_by("Price (High > Low)")
        assert catalog_page.get_current_sort_filter == "Price (High > Low)"

    @pytest.mark.skip("This test for local opencart version")
    @allure.story("Registration")
    @allure.title("User registration")
    def test_user_registration(self, driver):
        register_page = RegisterPage(driver)
        register_page.open_page()
        register_page.create_new_user()
        assert "Your Account Has Been Created!" in register_page.success_register_message
