import React from "react";
import Blogs from './Blogs';

const BlogPost = ({ Blog }) => {
    return (
            <div className="flex flex-col gap-y-2 mb-40">
                {Blog &&
                    Blog.map((data, index) => (
                        <div key={data.id}>
                            <Blogs author={data.author} title={data.title} date={data.date} description={data.description} lastUpdated={data.updated_at} id={data.id} content={data.content} audio={data.audio}/>
                        </div>
                    ))}
            </div>
    );
};

export default BlogPost;
