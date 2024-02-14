from src.models import Corpus


def main():
    folder_path = 'samples'  # Path to the folder containing sample text documents
    corpus = Corpus(folder_path, language='english')

    if corpus.documents:
        corpus_tfidf = corpus.tf_idf()

        for subject, tfidf_scores in corpus_tfidf.items():
            top_tfidf = dict(sorted(tfidf_scores.items(),
                             key=lambda item: item[1], reverse=True)[:5])
            print(f"Top 5 specific words for '{
                  subject}': {list(top_tfidf.keys())}")
    else:
        print("No documents found in the specified folder.")


if __name__ == "__main__":
    main()
