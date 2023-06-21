import React from "react";
import BlogPost from "../components/BlogPost";
import Header from "../components/Header";
import { BiArrowBack } from "react-icons/bi";
import { useLocation, useNavigate, useParams } from "react-router";
import ReactAudioPlayer from "react-audio-player";
const Blog = () => {
    const { blogId } = useParams();
    const navigate = useNavigate();
    const location = useLocation();
    const { title, content, audio } = location.state || {};
    return (
        <>
            <div className="bg-black">
                <Header />
                <div className="flex flex-col gap-y-2 px-12 py-8 min-h-screen text-white">
                    <button className="flex gap-2 items-center" onClick={() => navigate(-1)}>
                        <BiArrowBack />
                        Go Back
                    </button>
                    <div className="text-left mt-6 ">
                        <h1 className="text-lg my-4 px-20 font-bold text-center">{title}</h1>
                        <p>{content}</p>
                    </div>
                    <div className="mt-auto">
                        <ReactAudioPlayer src={audio} className="w-full rounded-sm" autoPlay controls />
                    </div>
                </div>
            </div>
        </>
    );
};

export default Blog;
