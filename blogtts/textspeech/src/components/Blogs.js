import React from "react";
import { useNavigate } from "react-router";
import { formatDate } from "../utilities/helper";
const Blog = ({ author, title, content, date, lastUpdated, id, audio }) => {
    // bg-[#f0f3f4]
    const navigate = useNavigate();
    return (
        <div
            className="cursor-pointer flex text-left flex-col gap-y-2  bg-[#131313] p-4 rounded-md text-white"
            onClick={() => navigate(`/blog/${id}`, { state: { title, content, audio } })}
        >
            <div className="flex justify-between">
                <p className="font-semibold">{author || "Adewale adekanye"}</p>
                <p>{formatDate(lastUpdated)}</p>
            </div>
            <p className="font-semibold line-clamp-1 text-lg">{title || "Health sector and matters"}</p>
            <p className="line-clamp-2">
                {content ||
                    "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Rem provident deserunt, eaque nam assumenda nisi officiis velit corporis? Possimus placeat hic accusantium velit corporis cupiditate consectetur vero nulla dolore officiis."}
            </p>
        </div>
    );
};

export default Blog;
