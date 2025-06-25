---

### ✅ 1. Create a New GitHub Repository

1. Go to [https://github.com](https://github.com)
2. Click **"New Repository"**
3. Enter:

   * **Repository name**: `scalable-json-hive-etl`
   * **Public** or **Private**
   * (✅ Optional) Add a `README.md` if you haven't already
4. Click **Create repository**

---

### ✅ 2. Push Code from Your Local System

Assuming your project is in:

```
C:\Users\saut7\IdeaProjects\scalable-json-hive-etl
```

Open your terminal and run:

```bash
cd C:\Users\saut7\IdeaProjects\scalable-json-hive-etl
```

Initialize Git:

```bash
git init
```

Add all files:

```bash
git add .
```

Commit them:

```bash
git commit -m "Initial commit: Spark4 ETL Project"
```

Connect to GitHub (replace `<your-username>` with your actual GitHub username):

```bash
git remote add origin https://github.com/<your-username>/scalable-json-hive-etl.git
```

Push to GitHub:

```bash
git push -u origin master
```

> ❗ If you created a repo with `main` as the default branch, use:

```bash
git push -u origin main
```

---

### ✅ 3. Confirm

Go to your GitHub repo page — you should now see all your files pushed!

---

### 💡 Optional: Add `.gitignore`

If you want to exclude virtual envs and compiled files, create a `.gitignore` in the root folder with:

```gitignore
.venv/
__pycache__/
*.pyc
warehouse/
```

Then:

```bash
git add .gitignore
git commit -m "Add .gitignore"
git push
```
