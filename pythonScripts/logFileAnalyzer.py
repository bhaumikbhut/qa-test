import re
from collections import Counter

log_file_path = 'file.log'

def analyze_log_file(log_file):
    try:
        total_requests = 0
        status_404_count = 0
        page_requests = Counter()
        ip_requests = Counter()

        with open(log_file, 'r') as file:
            for line in file:
                total_requests += 1
                match = re.match(r'^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S*)" (\d{3}) (\S+)', line)
                if match:
                    ip_address = match.group(1)
                    status_code = match.group(8)
                    requested_page = match.group(6)

            
                    if status_code == '404':
                        status_404_count += 1

                  
                    page_requests[requested_page] += 1

    
                    ip_requests[ip_address] += 1


        print(f"Total requests: {total_requests}")
        print(f"404 errors: {status_404_count}")

        print("\nMost requested pages:")
        for page, count in page_requests.most_common(10):
            print(f"{page}: {count} requests")

        print("\nIP addresses with most requests:")
        for ip, count in ip_requests.most_common(10):
            print(f"{ip}: {count} requests")

    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file}")
    except Exception as e:
        print(f"Error analyzing log file: {e}")

if __name__ == "__main__":
    print(f"Analyzing log file: {log_file_path}")
    analyze_log_file(log_file_path)