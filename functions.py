import json


def open_json(file) -> list:
    with open(file, encoding="utf-8") as f:
        json_data = json.load(f)

    return json_data


def write_json(file, data) -> None:
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def comments_count(posts_data, comments_data) -> list:
    comments_match = []
    for post in posts_data:
        for comment in comments_data:
            if comment["post_id"] == post["pk"]:
                comments_match.append(post["pk"])
            post["comments"] = comments_match.count(post["pk"])

    return posts_data


def string_crop(posts_data) -> list:
    for post in posts_data:
        post["content"] = post["content"][:50]

    return posts_data


def get_post(posts_data, post_id) -> dict:
    output_post = {}
    for post in posts_data:
        if post_id == post["pk"]:
            output_post = post

    return output_post


def get_tags(post) -> list:
    tags = []
    text = post["content"].split(" ")
    for word in text:
        if "#" in word:
            tag = word.replace("#", "")
            tags.append(tag)

    return tags
