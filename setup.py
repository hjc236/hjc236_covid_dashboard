from distutils.core import setup
setup(
    name = 'hjc236_covid_dashboard',
    packages = ['hjc236_covid_dashboard'],
    version = '0.1',
    license='MIT',
    description = 'hjc236_covid_dashboard is a python project which generates a web dashboard with COVID-19 data and relevant news articles.',
    author = 'hjc236',
    author_email = '',
    url = 'https://github.com/hjc236/hjc236_covid_dashboard',
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
    keywords = ['coronavirus', 'event-driven', 'dashboard'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
        'uk_covid19',
        'flask',
        'pytest'

    ],
    classifiers=[
        'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3.10',
    ],
)