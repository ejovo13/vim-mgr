import uvicorn

if __name__ == "__main__":
    uvicorn.run("nvim_remote:app", host="0.0.0.0", port=8881, reload=True)
    pass
