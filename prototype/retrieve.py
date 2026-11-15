"""Retrieval over the help-centre articles: chunk by '## ' heading, TF-IDF cosine, top-k above a minimum score."""
import glob, os, re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CHUNKS, _VEC, _MAT = [], None, None


def _load(kb_dir=None):
    global _CHUNKS, _VEC, _MAT
    _CHUNKS = []
    for path in sorted(glob.glob(os.path.join(kb_dir or os.path.join(ROOT, "kb"), "*.md"))):
        art = os.path.basename(path).replace(".md", "")
        text = open(path, encoding="utf-8").read()
        for sec in re.split(r"\n## ", text)[1:]:
            title, _, body = sec.partition("\n")
            _CHUNKS.append({"article": art, "section": title.strip(), "text": body.strip()})
    docs = [c["section"] + " " + c["text"] for c in _CHUNKS]
    _VEC = TfidfVectorizer(ngram_range=(1, 2), stop_words="english").fit(docs)
    _MAT = _VEC.transform(docs)


def top_k(query, k=3, min_score=0.05):
    if _VEC is None:
        _load()
    sims = cosine_similarity(_VEC.transform([query]), _MAT)[0]
    order = sims.argsort()[::-1][:k]
    return [dict(_CHUNKS[i], score=float(sims[i])) for i in order if sims[i] >= min_score]
