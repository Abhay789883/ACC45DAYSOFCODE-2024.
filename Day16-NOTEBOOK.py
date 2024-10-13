def calculate_notebooks(N):
    pages_per_kg = 1000
    pages_per_notebook = 100
    
    total_pages = N * pages_per_kg
    notebooks = total_pages // pages_per_notebook
    return notebooks

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        N = int(input())
        results.append(calculate_notebooks(N))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
