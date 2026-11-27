# 这次练习如何提交

姓名：LanMingqi；学号：26723811。

## 作业要求

老师要求新建一个 GitHub 仓库，运行 pickle 示例，并上传代码和实际生成的
pickle 文件。最后在微信群发送 **GitHub 仓库链接 + 姓名**。

## 本项目已准备的内容

四部分代码已整理在 `run_practice.py`，自定义类在 `grade_tracker.py`。
`load_saved.py` 可以在另一个 Python 进程里重新加载文件并预测，无须训练。
所有提交文件在同一层，网页上传时无需调整子文件夹。

实际执行结果看 `execution_log.txt`、`reload_log.txt` 和 `results.json`。

## GitHub 网页操作

1. 登录 GitHub，新建仓库，名称建议 `python-pickling-practice`。
2. 进入新仓库，点击 Add file -> Upload files。
3. 打开本地 `outputs/python-pickling-practice` 文件夹，将里面的全部文件拖入网页。
   注意包含 `.pkl`、`.joblib`、`.png` 和日志；不要只上传代码。
4. 点击 Commit changes。
5. 打开仓库首页，确认能看到这六个 pickle 文件：
   `fruits.pkl`、`scores.pkl`、`complex_data.pkl`、`ml_course_grades.pkl`、
   `ml_course_grades_updated.pkl`、`study_hours_model.pkl`。
   另外还应有 `study_hours_model.joblib` 和 `study_hours_model.png`。
6. 将仓库首页地址和姓名发到课程微信群，例如：

   姓名：LanMingqi
   仓库：复制你新建的仓库完整链接

本题的提交要求是代码与保存文件，不要求额外部署 Hugging Face。
附带的 ZIP 是便于下载的项目包；应解压后上传里面的文件。

## 自己再次运行

在项目文件夹中打开终端，使用 Python 3.11 或 3.12：

```bash
python -m pip install -r requirements.txt
python run_practice.py
python load_saved.py
```

重新运行会更新成绩对象的时间戳和运行记录，模型使用固定随机种子。
