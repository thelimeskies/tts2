import React, { useEffect, useState } from "react";
import ReactAudioPlayer from "react-audio-player";
import Header from "../components/Header";
import BlogPost from "../components/BlogPost";

const Home = () => {
    const [loading, setLoading] = useState(false);
    const [blogs, setBlogs] = useState("");
    const [audio, setAudio] = useState("");
    const [audioText, setAudioText] = useState("");
    const [textSize, setTextSize] = useState("");
    const fetchBlogs = async () => {
        setLoading("true");
        try {
            const base = "http://127.0.0.01:8000";
            const response = await fetch(`${base}/api/v1/scraped-articles/`, {
                methods: "GET",
                headers: { "Content-Type": "application/json" },
            });
            if (!response.ok) throw new Error("Cannot Load Blogs");
            setLoading(false);
            const data = await response.json();
            setLoading(false);
            setBlogs(data);
        } catch (error) {
            console.log(error);
        }
    };
    const convertText = async (e) => {
        if (!audioText) return alert("Cannot process audio without text");
        try {
            const response = await fetch("", {
                methods: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(audioText),
            });
            const data = await response.json();
            if (!response.ok) throw new Error("Couldn't convert audio file");
            //this below is meant to change the audio component state
            setAudio(data.audio);
            console.log("success");
        } catch (error) {
            console.log(error.message);
        }
    };
    const handleChange = (e) => {
        const text = e.target.value.length;
        setTextSize(text);
        setAudioText(text);
    };

    const items = [
        {
            id: 1,
            author: "John Doe",
            title: "GENOMICS' TRANSFORMATIVE ROLE IN CANCER DIAGNOSIS AND TREATMENT",
            content:
                "One of the most dangerous malignant diseases to people's lives and health is cancer . Cancer is a hereditary disease with a complex mult",
            description: "This is the first item in the array.",
            updated_at: "2023-05-07T08:46:00+01:00",
            date: "2023-05-07T08:46:00+01:00",
            audio: null,
        },
        {
            id: 2,
            author: "Jane Smith",
            title: "Item 2",
            description: "This is the second item in the array.",
            updated_at: "2023-05-07T08:46:00+01:00",
            date: "2023-05-07T08:46:00+01:00",
        },
        {
            id: 3,
            author: "Bob Johnson",
            title: "Item 3",
            description: "This is the third item in the array.",
            updated_at: "2023-05-07T08:46:00+01:00",
            date: "2023-05-07T08:46:00+01:00",
        },
        {
            id: 4,
            author: "Alice Lee",
            title: "Item 4",
            description: "This is the fourth item in the array.",
            updated_at: "2023-05-07T08:46:00+01:00",
            date: "2023-05-07T08:46:00+01:00",
        },
        {
            id: 5,
            author: "Tom Wilson",
            title: "Item 5",
            description: "This is the fifth item in the array.",
            updated_at: "2023-05-07T08:46:00+01:00",
            date: "2023-05-07T08:46:00+01:00",
        },
        {
            id: 6,
            author: "Sara Lee",
            title: "Item 6",
            description: "This is the sixth item in the array.",
            updated_at: "2023-05-07T08:46:00+01:00",
            date: "2023-05-07T08:46:00+01:00",
        },
        {
            id: 7,
            author: "Mike Brown",
            title: "Item 7",
            description: "This is the seventh item in the array.",
            updated_at: "2023-05-07T08:46:00+01:00",
            date: "2023-05-07T08:46:00+01:00",
        },
        {
            id: 8,
            author: "Emily Davis",
            title: "Item 8",
            description: "This is the eighth item in the array.",
            updated_at: "2023-05-07T08:46:00+01:00",
            date: "2023-05-07T08:46:00+01:00",
        },
    ];

    useEffect(() => {
        fetchBlogs();
    }, []);

    return (
        <div className="bg-black">
            <Header />
            <div className="flex gap-x-8 px-20 py-4 text-white">
                <div className="w-[50%]"></div>
                <div className=" flex justify-between w-[50%]">
                    <h1 className="text-xl uppercase font-semibold">Blog Posts</h1>
                    {/* <p className=" self-end">retrieved from ...</p> */}
                </div>
            </div>
            <div className="grid h-full grid-cols-2 px-12 gap-x-8 ">
                <div className="flex flex-col max-h-screen w-full px-4">
                    <div className="relative flex flex-col">
                        <textarea
                            className="rounded-md border border-gray-400 p-4"
                            maxLength={225}
                            onChange={(e) => handleChange(e)}
                        />
                        <h1 className="absolute bottom-2 left-2  ">{textSize || 0}/225</h1>
                        <button
                            className=" bg-gray-400 text-white font-semibold px-4 py-1 rounded-md absolute bottom-2 right-2"
                            onClick={convertText}
                        >
                            Translate Text
                        </button>
                    </div>
                    <div className="pt-3 w-full">
                        <ReactAudioPlayer
                            className="w-full rounded-sm"
                            src={audio}
                            autoPlay
                            controls
                        />
                    </div>
                </div>
                <div className=" h-screen overflow-auto">
                     <BlogPost Blog={items} />
                    {/* {blogs && !loading && <BlogPost Blog={blogs} />}
                    {!blogs && loading && "Blogs Loading ......"}
                    {!blogs && !loading && "NO BLOG POST FOUND"} */}
                </div>
            </div>
        </div>
    );
};

export default Home;
