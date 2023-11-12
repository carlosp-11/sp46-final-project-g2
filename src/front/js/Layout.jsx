import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import injectContext from "./store/appContext";
import ScrollToTop from "./component/scrollToTop";
import { BackendURL } from "./component/BackendURL.jsx";
// Import pages and component
import { Demo } from "./pages/demo";
import { Single } from "./pages/single";
import { Home } from "./pages/Home.jsx";
import { Navbarcarlos } from "./component/Navbarcarlos.jsx";
import { Footer } from "./component/Footer.jsx";
import { Login } from "./pages/Login.jsx";
import { Signup } from "./pages/Signup.jsx"
import { Form } from "./pages/Form.jsx";
import { DisclaimerView } from "./pages/DisclimerView.jsx";
import { PrivacyPolicyView } from "./pages/PrivacyPolicyView.jsx";
import { HorizontalCard } from "./component/HorizontalCard.jsx";
import { List } from "./pages/List.jsx";
import { PostEdit } from "./pages/PostEdit.jsx";
import { PostView } from "./pages/PostView.jsx";



// Create your first component
const Layout = () => {
    // The basename is used when your project is published in a subdirectory and not in the root of the domain.
    // You can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
    const basename = process.env.BASENAME || "";
    if(!process.env.BACKEND_URL || process.env.BACKEND_URL == "") return <BackendURL/ >;

    return (
        <div>
            <BrowserRouter basename={basename}>
                <ScrollToTop>
                    <Navbarcarlos />
                    <Routes>
                        <Route element={<Home />} path="/" />
                        <Route element={<Form/>} path="/form" />
                        <Route element={<Login />} path="/login" />
                        <Route element={<Signup />} path="/signup" />
                        <Route element={<Demo />} path="/demo" />
                        <Route element={<List />} path="/list" />
                        <Route element={<PostEdit />} path="/post-edit" />
                        <Route element={<PostView />} path="/post-view" />
                        <Route element={<HorizontalCard />} path="/horizontal-card" />
                        <Route element={<DisclaimerView />} path="/disclaimer-view" />
                        <Route element={<PrivacyPolicyView />} path="/privacy-policy-view" />
                        <Route element={<Single />} path="/single/:theid" />
                        <Route element={<h1>Not found!</h1>} />
                    </Routes>
                    <Footer />
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
