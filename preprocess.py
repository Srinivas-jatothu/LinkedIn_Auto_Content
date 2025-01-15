import json

def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    enriched_posts = []
    with open(raw_file_path, encoding="utf-8") as file:
        posts = json.load(file)
        # print(posts)
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)
    
    for epost in enriched_posts:
        print(epost)


def extract_metadata(text):
    return {
        'line_count':10,
        'language':'English',
        'tags':['mental health', 'Motivation']
    }

if __name__ == "__main__":
    process_posts(r"C:\Users\jsrin\OneDrive\Desktop\GenAi\Linkedin_Post_Generator\data\raw_post.json")