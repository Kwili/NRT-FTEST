---
description: |
    API documentation for modules: nrt-ftest, nrt-ftest.Mobile_tests, nrt-ftest.Mobile_tests.Screens, nrt-ftest.Mobile_tests.Screens.BotScreen, nrt-ftest.Mobile_tests.Screens.LoginScreen, nrt-ftest.Mobile_tests.Screens.MapScreen, nrt-ftest.Mobile_tests.Tests, nrt-ftest.Mobile_tests.Tests.botMobile, nrt-ftest.Mobile_tests.Tests.loginMobile, nrt-ftest.Mobile_tests.Tests.mapMobile, nrt-ftest.Mobile_tests.mobile_app, nrt-ftest.Website_tests, nrt-ftest.Website_tests.Pages, nrt-ftest.Website_tests.Pages.HomePage, nrt-ftest.Website_tests.Pages.LandingPage, nrt-ftest.Website_tests.Pages.MapPage, nrt-ftest.Website_tests.Tests, nrt-ftest.Website_tests.Tests.home, nrt-ftest.Website_tests.Tests.landing, nrt-ftest.Website_tests.Tests.map, nrt-ftest.Website_tests.website_app, nrt-ftest.main.

lang: en

classoption: oneside
geometry: margin=1in
papersize: a4

linkcolor: blue
links-as-notes: true
...


    
# Namespace `nrt-ftest` {#nrt-ftest}




    
## Sub-modules

* [nrt-ftest.Mobile_tests](#nrt-ftest.Mobile_tests)
* [nrt-ftest.Website_tests](#nrt-ftest.Website_tests)
* [nrt-ftest.main](#nrt-ftest.main)






    
# Module `nrt-ftest.Mobile_tests` {#nrt-ftest.Mobile_tests}




    
## Sub-modules

* [nrt-ftest.Mobile_tests.Screens](#nrt-ftest.Mobile_tests.Screens)
* [nrt-ftest.Mobile_tests.Tests](#nrt-ftest.Mobile_tests.Tests)
* [nrt-ftest.Mobile_tests.mobile_app](#nrt-ftest.Mobile_tests.mobile_app)






    
# Module `nrt-ftest.Mobile_tests.Screens` {#nrt-ftest.Mobile_tests.Screens}




    
## Sub-modules

* [nrt-ftest.Mobile_tests.Screens.BotScreen](#nrt-ftest.Mobile_tests.Screens.BotScreen)
* [nrt-ftest.Mobile_tests.Screens.LoginScreen](#nrt-ftest.Mobile_tests.Screens.LoginScreen)
* [nrt-ftest.Mobile_tests.Screens.MapScreen](#nrt-ftest.Mobile_tests.Screens.MapScreen)






    
# Module `nrt-ftest.Mobile_tests.Screens.BotScreen` {#nrt-ftest.Mobile_tests.Screens.BotScreen}







    
## Classes


    
### Class `BotScreen` {#nrt-ftest.Mobile_tests.Screens.BotScreen.BotScreen}




>     class BotScreen(
>         driver
>     )










    
#### Methods


    
##### Method `click_bot_tab` {#nrt-ftest.Mobile_tests.Screens.BotScreen.BotScreen.click_bot_tab}




>     def click_bot_tab(
>         self
>     )




    
##### Method `send_text` {#nrt-ftest.Mobile_tests.Screens.BotScreen.BotScreen.send_text}




>     def send_text(
>         self,
>         text
>     )






    
# Module `nrt-ftest.Mobile_tests.Screens.LoginScreen` {#nrt-ftest.Mobile_tests.Screens.LoginScreen}







    
## Classes


    
### Class `LoginScreen` {#nrt-ftest.Mobile_tests.Screens.LoginScreen.LoginScreen}




>     class LoginScreen(
>         driver
>     )










    
#### Methods


    
##### Method `click_login` {#nrt-ftest.Mobile_tests.Screens.LoginScreen.LoginScreen.click_login}




>     def click_login(
>         self
>     )




    
##### Method `fill_id` {#nrt-ftest.Mobile_tests.Screens.LoginScreen.LoginScreen.fill_id}




>     def fill_id(
>         self
>     )






    
# Module `nrt-ftest.Mobile_tests.Screens.MapScreen` {#nrt-ftest.Mobile_tests.Screens.MapScreen}







    
## Classes


    
### Class `MapScreen` {#nrt-ftest.Mobile_tests.Screens.MapScreen.MapScreen}




>     class MapScreen(
>         driver
>     )










    
#### Methods


    
##### Method `choose_transport` {#nrt-ftest.Mobile_tests.Screens.MapScreen.MapScreen.choose_transport}




>     def choose_transport(
>         self,
>         index
>     )




    
##### Method `click_allow_geo` {#nrt-ftest.Mobile_tests.Screens.MapScreen.MapScreen.click_allow_geo}




>     def click_allow_geo(
>         self
>     )




    
##### Method `click_najma` {#nrt-ftest.Mobile_tests.Screens.MapScreen.MapScreen.click_najma}




>     def click_najma(
>         self
>     )




    
##### Method `click_plus` {#nrt-ftest.Mobile_tests.Screens.MapScreen.MapScreen.click_plus}




>     def click_plus(
>         self
>     )




    
##### Method `click_rechercher` {#nrt-ftest.Mobile_tests.Screens.MapScreen.MapScreen.click_rechercher}




>     def click_rechercher(
>         self
>     )




    
##### Method `click_return` {#nrt-ftest.Mobile_tests.Screens.MapScreen.MapScreen.click_return}




>     def click_return(
>         self
>     )




    
##### Method `click_transport` {#nrt-ftest.Mobile_tests.Screens.MapScreen.MapScreen.click_transport}




>     def click_transport(
>         self
>     )




    
##### Method `click_votre_position` {#nrt-ftest.Mobile_tests.Screens.MapScreen.MapScreen.click_votre_position}




>     def click_votre_position(
>         self
>     )




    
##### Method `has_found_itinary` {#nrt-ftest.Mobile_tests.Screens.MapScreen.MapScreen.has_found_itinary}




>     def has_found_itinary(
>         self
>     )




    
##### Method `write_position` {#nrt-ftest.Mobile_tests.Screens.MapScreen.MapScreen.write_position}




>     def write_position(
>         self,
>         location
>     )






    
# Module `nrt-ftest.Mobile_tests.Tests` {#nrt-ftest.Mobile_tests.Tests}




    
## Sub-modules

* [nrt-ftest.Mobile_tests.Tests.botMobile](#nrt-ftest.Mobile_tests.Tests.botMobile)
* [nrt-ftest.Mobile_tests.Tests.loginMobile](#nrt-ftest.Mobile_tests.Tests.loginMobile)
* [nrt-ftest.Mobile_tests.Tests.mapMobile](#nrt-ftest.Mobile_tests.Tests.mapMobile)






    
# Module `nrt-ftest.Mobile_tests.Tests.botMobile` {#nrt-ftest.Mobile_tests.Tests.botMobile}







    
## Classes


    
### Class `BotMobileTest` {#nrt-ftest.Mobile_tests.Tests.botMobile.BotMobileTest}




>     class BotMobileTest(
>         methodName='runTest'
>     )


A class whose instances are single test cases.

By default, the test code itself should be placed in a method named
'runTest'.

If the fixture may be used for many test cases, create as
many test methods as are needed. When instantiating such a TestCase
subclass, specify in the constructor arguments the name of the test method
that the instance is to execute.

Test authors should subclass TestCase for their own tests. Construction
and deconstruction of the test's environment ('fixture') can be
implemented by overriding the 'setUp' and 'tearDown' methods respectively.

If it is necessary to override the __init__ method, the base class
__init__ method must always be called. It is important that subclasses
should not change the signature of their __init__ method, since instances
of the classes are instantiated automatically by parts of the framework
in order to be run.

When subclassing TestCase, you can set these attributes:
* failureException: determines which exception will be raised when
    the instance's assertion methods fail; test methods raising this
    exception will be deemed to have 'failed' rather than 'errored'.
* longMessage: determines whether long messages (including repr of
    objects used in assert methods) will be printed on failure in *addition*
    to any explicit message passed.
* maxDiff: sets the maximum length of a diff in failure messages
    by assert methods using difflib. It is looked up as an instance
    attribute so can be configured by individual tests if required.

Create an instance of the class that will use the named test
method when executed. Raises a ValueError if the instance does
not have a method with the specified name.


    
#### Ancestors (in MRO)

* [unittest.case.TestCase](#unittest.case.TestCase)





    
#### Static methods


    
##### `Method setUpClass` {#nrt-ftest.Mobile_tests.Tests.botMobile.BotMobileTest.setUpClass}




>     def setUpClass()


Hook method for setting up class fixture before running tests in the class.

    
##### `Method tearDownClass` {#nrt-ftest.Mobile_tests.Tests.botMobile.BotMobileTest.tearDownClass}




>     def tearDownClass()


Hook method for deconstructing the class fixture after running all tests in the class.


    
#### Methods


    
##### Method `test_01_bot` {#nrt-ftest.Mobile_tests.Tests.botMobile.BotMobileTest.test_01_bot}




>     def test_01_bot(
>         self
>     )






    
# Module `nrt-ftest.Mobile_tests.Tests.loginMobile` {#nrt-ftest.Mobile_tests.Tests.loginMobile}







    
## Classes


    
### Class `LoginMobileTest` {#nrt-ftest.Mobile_tests.Tests.loginMobile.LoginMobileTest}




>     class LoginMobileTest(
>         methodName='runTest'
>     )


A class whose instances are single test cases.

By default, the test code itself should be placed in a method named
'runTest'.

If the fixture may be used for many test cases, create as
many test methods as are needed. When instantiating such a TestCase
subclass, specify in the constructor arguments the name of the test method
that the instance is to execute.

Test authors should subclass TestCase for their own tests. Construction
and deconstruction of the test's environment ('fixture') can be
implemented by overriding the 'setUp' and 'tearDown' methods respectively.

If it is necessary to override the __init__ method, the base class
__init__ method must always be called. It is important that subclasses
should not change the signature of their __init__ method, since instances
of the classes are instantiated automatically by parts of the framework
in order to be run.

When subclassing TestCase, you can set these attributes:
* failureException: determines which exception will be raised when
    the instance's assertion methods fail; test methods raising this
    exception will be deemed to have 'failed' rather than 'errored'.
* longMessage: determines whether long messages (including repr of
    objects used in assert methods) will be printed on failure in *addition*
    to any explicit message passed.
* maxDiff: sets the maximum length of a diff in failure messages
    by assert methods using difflib. It is looked up as an instance
    attribute so can be configured by individual tests if required.

Create an instance of the class that will use the named test
method when executed. Raises a ValueError if the instance does
not have a method with the specified name.


    
#### Ancestors (in MRO)

* [unittest.case.TestCase](#unittest.case.TestCase)





    
#### Static methods


    
##### `Method setUpClass` {#nrt-ftest.Mobile_tests.Tests.loginMobile.LoginMobileTest.setUpClass}




>     def setUpClass()


Hook method for setting up class fixture before running tests in the class.

    
##### `Method tearDownClass` {#nrt-ftest.Mobile_tests.Tests.loginMobile.LoginMobileTest.tearDownClass}




>     def tearDownClass()


Hook method for deconstructing the class fixture after running all tests in the class.


    
#### Methods


    
##### Method `test_01_No_Login` {#nrt-ftest.Mobile_tests.Tests.loginMobile.LoginMobileTest.test_01_No_Login}




>     def test_01_No_Login(
>         self
>     )




    
##### Method `test_02_Loggin` {#nrt-ftest.Mobile_tests.Tests.loginMobile.LoginMobileTest.test_02_Loggin}




>     def test_02_Loggin(
>         self
>     )






    
# Module `nrt-ftest.Mobile_tests.Tests.mapMobile` {#nrt-ftest.Mobile_tests.Tests.mapMobile}







    
## Classes


    
### Class `MapMobileTest` {#nrt-ftest.Mobile_tests.Tests.mapMobile.MapMobileTest}




>     class MapMobileTest(
>         methodName='runTest'
>     )


A class whose instances are single test cases.

By default, the test code itself should be placed in a method named
'runTest'.

If the fixture may be used for many test cases, create as
many test methods as are needed. When instantiating such a TestCase
subclass, specify in the constructor arguments the name of the test method
that the instance is to execute.

Test authors should subclass TestCase for their own tests. Construction
and deconstruction of the test's environment ('fixture') can be
implemented by overriding the 'setUp' and 'tearDown' methods respectively.

If it is necessary to override the __init__ method, the base class
__init__ method must always be called. It is important that subclasses
should not change the signature of their __init__ method, since instances
of the classes are instantiated automatically by parts of the framework
in order to be run.

When subclassing TestCase, you can set these attributes:
* failureException: determines which exception will be raised when
    the instance's assertion methods fail; test methods raising this
    exception will be deemed to have 'failed' rather than 'errored'.
* longMessage: determines whether long messages (including repr of
    objects used in assert methods) will be printed on failure in *addition*
    to any explicit message passed.
* maxDiff: sets the maximum length of a diff in failure messages
    by assert methods using difflib. It is looked up as an instance
    attribute so can be configured by individual tests if required.

Create an instance of the class that will use the named test
method when executed. Raises a ValueError if the instance does
not have a method with the specified name.


    
#### Ancestors (in MRO)

* [unittest.case.TestCase](#unittest.case.TestCase)





    
#### Static methods


    
##### `Method setUpClass` {#nrt-ftest.Mobile_tests.Tests.mapMobile.MapMobileTest.setUpClass}




>     def setUpClass()


Hook method for setting up class fixture before running tests in the class.

    
##### `Method tearDownClass` {#nrt-ftest.Mobile_tests.Tests.mapMobile.MapMobileTest.tearDownClass}




>     def tearDownClass()


Hook method for deconstructing the class fixture after running all tests in the class.


    
#### Methods


    
##### Method `test_01_map_feet` {#nrt-ftest.Mobile_tests.Tests.mapMobile.MapMobileTest.test_01_map_feet}




>     def test_01_map_feet(
>         self
>     )




    
##### Method `test_02_map_car` {#nrt-ftest.Mobile_tests.Tests.mapMobile.MapMobileTest.test_02_map_car}




>     def test_02_map_car(
>         self
>     )




    
##### Method `test_03_map_adress_written` {#nrt-ftest.Mobile_tests.Tests.mapMobile.MapMobileTest.test_03_map_adress_written}




>     def test_03_map_adress_written(
>         self
>     )




    
##### Method `test_04_map_display_details` {#nrt-ftest.Mobile_tests.Tests.mapMobile.MapMobileTest.test_04_map_display_details}




>     def test_04_map_display_details(
>         self
>     )






    
# Module `nrt-ftest.Mobile_tests.mobile_app` {#nrt-ftest.Mobile_tests.mobile_app}






    
## Functions


    
### Function `run` {#nrt-ftest.Mobile_tests.mobile_app.run}




>     def run()







    
# Module `nrt-ftest.Website_tests` {#nrt-ftest.Website_tests}




    
## Sub-modules

* [nrt-ftest.Website_tests.Pages](#nrt-ftest.Website_tests.Pages)
* [nrt-ftest.Website_tests.Tests](#nrt-ftest.Website_tests.Tests)
* [nrt-ftest.Website_tests.website_app](#nrt-ftest.Website_tests.website_app)






    
# Module `nrt-ftest.Website_tests.Pages` {#nrt-ftest.Website_tests.Pages}




    
## Sub-modules

* [nrt-ftest.Website_tests.Pages.HomePage](#nrt-ftest.Website_tests.Pages.HomePage)
* [nrt-ftest.Website_tests.Pages.LandingPage](#nrt-ftest.Website_tests.Pages.LandingPage)
* [nrt-ftest.Website_tests.Pages.MapPage](#nrt-ftest.Website_tests.Pages.MapPage)






    
# Module `nrt-ftest.Website_tests.Pages.HomePage` {#nrt-ftest.Website_tests.Pages.HomePage}







    
## Classes


    
### Class `HomePage` {#nrt-ftest.Website_tests.Pages.HomePage.HomePage}




>     class HomePage(
>         driver
>     )










    
#### Methods


    
##### Method `click_chat_card` {#nrt-ftest.Website_tests.Pages.HomePage.HomePage.click_chat_card}




>     def click_chat_card(
>         self
>     )




    
##### Method `click_landing_button` {#nrt-ftest.Website_tests.Pages.HomePage.HomePage.click_landing_button}




>     def click_landing_button(
>         self
>     )




    
##### Method `click_map_card` {#nrt-ftest.Website_tests.Pages.HomePage.HomePage.click_map_card}




>     def click_map_card(
>         self
>     )






    
# Module `nrt-ftest.Website_tests.Pages.LandingPage` {#nrt-ftest.Website_tests.Pages.LandingPage}







    
## Classes


    
### Class `LandingPage` {#nrt-ftest.Website_tests.Pages.LandingPage.LandingPage}




>     class LandingPage(
>         driver
>     )










    
#### Methods


    
##### Method `click_app_apercu_link` {#nrt-ftest.Website_tests.Pages.LandingPage.LandingPage.click_app_apercu_link}




>     def click_app_apercu_link(
>         self
>     )




    
##### Method `click_chat_widget` {#nrt-ftest.Website_tests.Pages.LandingPage.LandingPage.click_chat_widget}




>     def click_chat_widget(
>         self
>     )




    
##### Method `click_home` {#nrt-ftest.Website_tests.Pages.LandingPage.LandingPage.click_home}




>     def click_home(
>         self
>     )




    
##### Method `click_map` {#nrt-ftest.Website_tests.Pages.LandingPage.LandingPage.click_map}




>     def click_map(
>         self
>     )




    
##### Method `click_navbar_app_link` {#nrt-ftest.Website_tests.Pages.LandingPage.LandingPage.click_navbar_app_link}




>     def click_navbar_app_link(
>         self
>     )






    
# Module `nrt-ftest.Website_tests.Pages.MapPage` {#nrt-ftest.Website_tests.Pages.MapPage}







    
## Classes


    
### Class `MapPage` {#nrt-ftest.Website_tests.Pages.MapPage.MapPage}




>     class MapPage(
>         driver
>     )










    
#### Methods


    
##### Method `click_bus` {#nrt-ftest.Website_tests.Pages.MapPage.MapPage.click_bus}




>     def click_bus(
>         self
>     )




    
##### Method `click_car` {#nrt-ftest.Website_tests.Pages.MapPage.MapPage.click_car}




>     def click_car(
>         self
>     )




    
##### Method `click_hospital` {#nrt-ftest.Website_tests.Pages.MapPage.MapPage.click_hospital}




>     def click_hospital(
>         self
>     )




    
##### Method `click_walk` {#nrt-ftest.Website_tests.Pages.MapPage.MapPage.click_walk}




>     def click_walk(
>         self
>     )




    
##### Method `move_slider` {#nrt-ftest.Website_tests.Pages.MapPage.MapPage.move_slider}




>     def move_slider(
>         self,
>         offset
>     )




    
##### Method `no_ininary_founded_handler` {#nrt-ftest.Website_tests.Pages.MapPage.MapPage.no_ininary_founded_handler}




>     def no_ininary_founded_handler(
>         self,
>         xpath
>     )




    
##### Method `write_position` {#nrt-ftest.Website_tests.Pages.MapPage.MapPage.write_position}




>     def write_position(
>         self
>     )




    
##### Method `zoom_in` {#nrt-ftest.Website_tests.Pages.MapPage.MapPage.zoom_in}




>     def zoom_in(
>         self
>     )




    
##### Method `zoom_out` {#nrt-ftest.Website_tests.Pages.MapPage.MapPage.zoom_out}




>     def zoom_out(
>         self
>     )






    
# Module `nrt-ftest.Website_tests.Tests` {#nrt-ftest.Website_tests.Tests}




    
## Sub-modules

* [nrt-ftest.Website_tests.Tests.home](#nrt-ftest.Website_tests.Tests.home)
* [nrt-ftest.Website_tests.Tests.landing](#nrt-ftest.Website_tests.Tests.landing)
* [nrt-ftest.Website_tests.Tests.map](#nrt-ftest.Website_tests.Tests.map)






    
# Module `nrt-ftest.Website_tests.Tests.home` {#nrt-ftest.Website_tests.Tests.home}







    
## Classes


    
### Class `HomeTest` {#nrt-ftest.Website_tests.Tests.home.HomeTest}




>     class HomeTest(
>         methodName='runTest'
>     )


Home Page Test.

Create an instance of the class that will use the named test
method when executed. Raises a ValueError if the instance does
not have a method with the specified name.


    
#### Ancestors (in MRO)

* [unittest.case.TestCase](#unittest.case.TestCase)





    
#### Static methods


    
##### `Method setUpClass` {#nrt-ftest.Website_tests.Tests.home.HomeTest.setUpClass}




>     def setUpClass()


Hook method for setting up class fixture before running tests in the class.

    
##### `Method tearDownClass` {#nrt-ftest.Website_tests.Tests.home.HomeTest.tearDownClass}




>     def tearDownClass()


Hook method for deconstructing the class fixture after running all tests in the class.


    
#### Methods


    
##### Method `test_chat_link` {#nrt-ftest.Website_tests.Tests.home.HomeTest.test_chat_link}




>     def test_chat_link(
>         self
>     )


test chat link.

    
##### Method `test_landing_link` {#nrt-ftest.Website_tests.Tests.home.HomeTest.test_landing_link}




>     def test_landing_link(
>         self
>     )


test landing link.

    
##### Method `test_map_link` {#nrt-ftest.Website_tests.Tests.home.HomeTest.test_map_link}




>     def test_map_link(
>         self
>     )


test map link.



    
# Module `nrt-ftest.Website_tests.Tests.landing` {#nrt-ftest.Website_tests.Tests.landing}







    
## Classes


    
### Class `LandingTest` {#nrt-ftest.Website_tests.Tests.landing.LandingTest}




>     class LandingTest(
>         methodName='runTest'
>     )


Landing Page Test.

Create an instance of the class that will use the named test
method when executed. Raises a ValueError if the instance does
not have a method with the specified name.


    
#### Ancestors (in MRO)

* [unittest.case.TestCase](#unittest.case.TestCase)





    
#### Static methods


    
##### `Method setUpClass` {#nrt-ftest.Website_tests.Tests.landing.LandingTest.setUpClass}




>     def setUpClass()


Hook method for setting up class fixture before running tests in the class.

    
##### `Method tearDownClass` {#nrt-ftest.Website_tests.Tests.landing.LandingTest.tearDownClass}




>     def tearDownClass()


Hook method for deconstructing the class fixture after running all tests in the class.


    
#### Methods


    
##### Method `test_apercu` {#nrt-ftest.Website_tests.Tests.landing.LandingTest.test_apercu}




>     def test_apercu(
>         self
>     )


Apercu section tests.

    
##### Method `test_chat_landing` {#nrt-ftest.Website_tests.Tests.landing.LandingTest.test_chat_landing}




>     def test_chat_landing(
>         self
>     )


Chat widget in landing.

    
##### Method `test_check_navbar` {#nrt-ftest.Website_tests.Tests.landing.LandingTest.test_check_navbar}




>     def test_check_navbar(
>         self
>     )


Navbar tests.



    
# Module `nrt-ftest.Website_tests.Tests.map` {#nrt-ftest.Website_tests.Tests.map}







    
## Classes


    
### Class `MapTest` {#nrt-ftest.Website_tests.Tests.map.MapTest}




>     class MapTest(
>         methodName='runTest'
>     )


A class whose instances are single test cases.

By default, the test code itself should be placed in a method named
'runTest'.

If the fixture may be used for many test cases, create as
many test methods as are needed. When instantiating such a TestCase
subclass, specify in the constructor arguments the name of the test method
that the instance is to execute.

Test authors should subclass TestCase for their own tests. Construction
and deconstruction of the test's environment ('fixture') can be
implemented by overriding the 'setUp' and 'tearDown' methods respectively.

If it is necessary to override the __init__ method, the base class
__init__ method must always be called. It is important that subclasses
should not change the signature of their __init__ method, since instances
of the classes are instantiated automatically by parts of the framework
in order to be run.

When subclassing TestCase, you can set these attributes:
* failureException: determines which exception will be raised when
    the instance's assertion methods fail; test methods raising this
    exception will be deemed to have 'failed' rather than 'errored'.
* longMessage: determines whether long messages (including repr of
    objects used in assert methods) will be printed on failure in *addition*
    to any explicit message passed.
* maxDiff: sets the maximum length of a diff in failure messages
    by assert methods using difflib. It is looked up as an instance
    attribute so can be configured by individual tests if required.

Create an instance of the class that will use the named test
method when executed. Raises a ValueError if the instance does
not have a method with the specified name.


    
#### Ancestors (in MRO)

* [unittest.case.TestCase](#unittest.case.TestCase)





    
#### Static methods


    
##### `Method setUpClass` {#nrt-ftest.Website_tests.Tests.map.MapTest.setUpClass}




>     def setUpClass()


Hook method for setting up class fixture before running tests in the class.

    
##### `Method tearDownClass` {#nrt-ftest.Website_tests.Tests.map.MapTest.tearDownClass}




>     def tearDownClass()


Hook method for deconstructing the class fixture after running all tests in the class.


    
#### Methods


    
##### Method `test_find_itinary` {#nrt-ftest.Website_tests.Tests.map.MapTest.test_find_itinary}




>     def test_find_itinary(
>         self
>     )


Test find itinary.

Write adress and click on all tranport available.

    
##### Method `test_radius` {#nrt-ftest.Website_tests.Tests.map.MapTest.test_radius}




>     def test_radius(
>         self
>     )


Test radius.

Test radius slider.

    
##### Method `test_zoom` {#nrt-ftest.Website_tests.Tests.map.MapTest.test_zoom}




>     def test_zoom(
>         self
>     )


Test map zoom.

Check that the user can zoom.



    
# Module `nrt-ftest.Website_tests.website_app` {#nrt-ftest.Website_tests.website_app}






    
## Functions


    
### Function `run` {#nrt-ftest.Website_tests.website_app.run}




>     def run()







    
# Module `nrt-ftest.main` {#nrt-ftest.main}








-----
Generated by *pdoc* 0.8.4 (<https://pdoc3.github.io>).
