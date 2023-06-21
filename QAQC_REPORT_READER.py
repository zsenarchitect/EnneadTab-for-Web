import os
import json
import logging


import pickle
from PyPDF2 import PdfReader
# from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from dotenv import load_dotenv


# read the json file and process accordingly. Save the report back to json file.


class Solution:

    def process_pdf(self, file):
        pdf_reader = PdfReader(file)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        logging.info(text)
        self.process_text(text)

    def process_text(self, text):

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)

        embeddings = OpenAIEmbeddings(openai_api_key=self.KEY)
        VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
        with open(self.local_embeding, "wb") as f:
            pickle.dump(VectorStore, f)

        self.vectors = VectorStore

    @property
    def local_embeding(self):
        return self.get_file_in_dump_folder(f"{self.store_name}.pkl")

    def is_vector_store_exists(self):

        if os.path.exists(self.local_embeding):
            with open(self.local_embeding, "rb") as f:
                self.vectors = pickle.load(f)
            return True
        return False

    def get_response(self, query):

        docs = self.vectors.similarity_search(query=query, k=5)

        llm = OpenAI(openai_api_key=self.KEY)
        chain = load_qa_chain(llm=llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=query)
            print(cb)

        return response

    def get_data_file(self):
        return self.get_file_in_dump_folder("QAQC_REPORT_DATA.json")

    def get_file_in_dump_folder(self, file):

        return "{}\Documents\EnneadTab Settings\Local Copy Dump\{}".format(os.environ["USERPROFILE"], file)

    def main(self):
        file = self.get_data_file()
        with open(file, 'r') as f:
            # get dictionary from json file
            data = json.load(f)

        self.KEY = data.get('api_key')
        # this should be controled from Revit side to maintain consiststn over multiple query
        self.store_name = data.get('store_name')
        print(self.store_name)
        if not self.is_vector_store_exists():
            print("vect stroe no existent")
            logging.info("vector store not exists")
            method = data.get('method')
            if method == 'pdf':
                report_address = data["qaqc_file"]
                self.process_pdf(report_address)
            elif method == 'text':
                self.process_text(data.get("`qaqc_text"))

        response = self.get_response(data.get("query"))

        data["response"] = response
        data["direction"] = "OUT"
        with open(file, 'w') as f:
            # get dictionary from json file
            json.dump(data, f)


if __name__ == '__main__':
    Solution().main()
    print("done!")
