gedit用flymake的な何か「gfly」
	-- something like flymake for gedit "gfly" --
	for gedit 3

![Screenshot](http://github.com/utisam/gfly/blob/master/Screenshot.png?raw=true "Screenshot")

	使い方(How to use)
		gfly.pluginとgflyフォルダを~/.gnome2/gedit/pluginsにコピー
		copy "gfly.plugin" and "gfly/" to ~/.local/share/gedit/plugins/
		
			~(home)/
				.local/
					share/
						gedit/
							plugins/
								gfly.plugin
								gfly/
		
		編集→設定→プラグインでgflyを有効にする
		"edit"->"Preference"->"Plugins" and check "gfly"
		
		geditでC言語のプログラムを書く
		write *.c using gedit
		
		間違える
		make a mistake
		
		保存する
		Ctrl + S
		
		赤線が出る
		Get underlined
		
		直す
		fix
		
		カーソルをエラーに合わせるとtooltipが出ます
		appear tooltip when you put cursor on error
		
	注意(Notes)
		C言語での利用にはgccが必要です
		you need "gcc" for C
		
		C++での利用にはg++が必要です
		you need "g++" for C++
		
		Javaでの利用にはjavacが必要です
		you need "javac" for Java
		
		Javascriptでの利用にはgjslintが必要です
		you need "gjslint" for Javascript
		
		Pythonでの利用にはpyflakesもしくはpylintが必要です
		you need "pyflakes" or "pylint" for Python
		デフォルトではpyflakesを利用します
		default is "pyflakes"
		
		C#での利用にはgmcsが必要です
		you need "gmcs" for C#
		
		Perlでの利用にはperlが必要です
		you need "perl" for Perl
		
		PHPでの利用にはphpが必要です
		you need "php" for PHP
		
		Rubyでの利用にはrubyが必要です
		you need "ruby" for Ruby
		
		LaTeXでの利用にはlacheckが必要です
		you need "lacheck" for LaTeX
		
		noseを利用すると，現在利用可能なエラージェネレータがわかります
		you can know available error generators by "nose"
		
			$ nosetests generatorTest.py
		
	キーバインディングを変更したい(You want to change key binding)
		__init__.pyを編集
		edit __init__.py
		
		geditを再起動
		restert gedit
	
	言語を増やしたい(You want to use other language)
		「なんとかErrorGenerator.py」を追加してください
		add "---ErrorGenerator.py"
		
		「settings.py」の「errorGenerator」にインスタンスを追加するとたぶんうまくいきます
		add that instance to "errorGenerator" of "settings.py", and maybe success
	
	書いた人(Author)
		Masatoshi Tsushima
		Twitter: @utisam

	変更履歴(Change Log)
		bashに対応
		gjslintに対応
		pyflakes, rubyに対応
		pycheckerからpylintに変更
		perlとPHPを追加
		C++とJavaとPython
		Cのみで作成

