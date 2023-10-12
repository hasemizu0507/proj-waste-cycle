from flask import Blueprint

# 識別名をcrudにしてBlueprintオブジェクトを生成
#
# テンプレートフォルダーは同じディレクトリの'templates'
# staticフォルダーは同じディレクトリの'static_crud'
crud = Blueprint(
    'crud',
    __name__,
    template_folder='templates',
    static_folder='static_crud',
)

"""投稿ページのログイン画面のルーティングとビューの定義
"""
from flask import render_template, url_for, redirect, session
from app.crud import forms  # app/crud/forms.pyをインポート
from app.app import app     # app/app.pyからappをインポート

@crud.route('/admincreate', methods=['GET', 'POST'])
def login():
    # フォームクラスAdminFormのインスタンスを生成
    form = forms.AdminForm()
    # session['logged_in']の値をFalseにする
    session['logged_in'] = False

    # ログイン画面のsubmitボタンがクリックされたときの処理
    if form.validate_on_submit():
        # ログイン画面に入力されたユーザー名とパスワードを
        # settings.pyのUSERNAMEとPASSWORDの値と照合する
        if form.username.data != app.config['USERNAME'] \
        or form.password.data != app.config['PASSWORD']:
            # 認証できない場合は再度login.htmlをレンダリングして
            # フォームクラスのインスタンスformを引き渡す
            return render_template('login.html', form=form)
        else:
            # 認証できた場合はsession['logged_in']をTrueにして
            # crud.articleにリダイレクトする
            session['logged_in'] = True
            return redirect(url_for('crud.article'))
        
    # ログイン画面へのアクセスは、login.htmlをレンダリングして
    # AdminFormのインスタンスformを引き渡す
    return render_template('login.html', form=form)

"""投稿ページのルーティングとビューの定義
"""
from app import models # app/models.pyをインポート
from app.app import db # app/app.pyからdbをインポート

@crud.route('/post', methods=['GET', 'POST'])
def article():
    # session['logged_in']がTrueでなければ
    # ログイン画面にリダイレクト
    if not session.get('logged_in'):
        return redirect(url_for('crud.login'))
    
    # フォームクラスArticlePostのインスタンスを生成
    form_art = forms.ArticlePost()

    # 投稿ページのsubmitボタンが押されたときの処理
    if form_art.validate_on_submit():
        # モデルクラスBlogpostのインスタンス生成
        blogpost = models.Blogpost(
            # フォームのpost_titleに入力されたデータを取得して
            # Blogpostのtitleフィールドに格納
            title=form_art.post_title.data,
            # フォームのpost_contentsに入力されたデータを取得して
            # Blogpostのcontentsフィールドに格納
            contents=form_art.post_contents.data,
        )
        # BlogpostオブジェクトをRecordのデータとして
        # データベースのテーブルに追加
        db.session.add(blogpost)
        # データベースを更新
        db.session.commit()
        # session['logged_in']をNoneにする
        session.pop(url_for('crud.login'))
        # 処理完了後、ログイン画面にリダイレクト
        return redirect(url_for('crud.login'))

    # 投稿ページへのアクセスは、post.htmlをレンダリングして
    # ArticlePostのインスタンスform_artを引き渡す
    return render_template('post.html', form=form_art)